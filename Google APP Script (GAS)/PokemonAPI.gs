function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu("Pokemon")
  .addItem('List Generation I', 'listGenerationI')
  .addItem('List Generation II', 'listGenerationII')
  .addItem('List Generation III', 'listGenerationIII')
  .addToUi();
}

function listGenerationI() {
  generatePokemonGenerationList(1);
}

function listGenerationII() {
  generatePokemonGenerationList(2);
}

function listGenerationIII() {
  generatePokemonGenerationList(3);
}

function generatePokemonGenerationList(gen) {
  var sheet = createNewSheet_("Generation "+ gen);
  var responseData = fetchData_("https://pokeapi.co/api/v2/generation/" + gen);

  var pokemons = responseData['pokemon_species'];
  var resourceDataList = [];

  var fetchLimit = pokemons.length; // should be pokemons.length
  for (var i = 0; i < fetchLimit; i++) {
    resourceDataList.push(fetchData_(pokemons[i]['url']));
  }

  var keys = Object.keys(resourceDataList[0]);
  Logger.log(keys);  

  fillSheetWithData_(resourceDataList, keys, sheet);
  formatRowHeader_();
  formatColumnHeader_();
  formatDataset_();
}

// Helper function that Returns cell index of column given key
function findIndex_(key) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  Logger.log("Finding column : " + key + " from " + sheet.getName());

  var headerRange = sheet.getRange(1, 1, 1, sheet.getLastColumn());
  var headerValues = headerRange.getValues();
  
  for (var column = 1; column <= headerValues[0].length; column++) {
    if (headerValues[0][column - 1] === key) {
      return column;
    }
  }
  
  return -1;
}

function formatRowHeader_(){
  var sheet = SpreadsheetApp.getActiveSheet();
  
  var headerRange = sheet.getRange(1, 1, 1, sheet.getLastColumn());
  headerRange
    .setFontWeight('bold')
    .setFontColor('#ffff')
    .setBackground('#6CD4FF')
    .setBorder(true, true, true, true, null, null, null, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
}

function formatColumnHeader_() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var numRows = sheet.getDataRange().getLastRow() - 1; // First is the column
  var columnHeaderRange = sheet.getRange(2, 1, numRows, 1);
  
  columnHeaderRange
    .setFontWeight('bold')
    .setFontStyle('italic');
  setFirstColumnToName_(columnHeaderRange, numRows);
}

function setFirstColumnToName_(headerRange, numRows){
  var nameIndex = findIndex_('name');
  if (nameIndex < 0) {
    Logger.log("Index not found!");
    return;
  }
  var headerColIndex = 1;
  var nameRange = headerRange.offset(0, nameIndex - headerColIndex);

  var headerValues = headerRange.getValues();
  var nameValues = nameRange.getValues();

  // Fillup the header values with the our target name values.
  for (var row = 0; row < numRows; row++) {
    headerValues[row][0] = nameValues[row][0];
  }
  headerRange.setValues(headerValues);

  // Rename Column Header
  SpreadsheetApp.getActiveSheet().getRange(1, 1).setValue('name');

  // Delete name column
  SpreadsheetApp.getActiveSheet().deleteColumn(nameIndex);
}

/**
 * Formats the sheet data, excluding the header row and column.
 * Applies a border and banding, formats the 'release_date'
 * column, and auto-sizes the rows and columns.
 */
function formatDataset_() {
  // Get the active sheet and data range.
  var sheet = SpreadsheetApp.getActiveSheet(); 
  var fullDataRange = sheet.getDataRange();

  // Apply row banding to the data, excluding the header
  // row and column. Only apply the banding if the range
  // doesn't already have a banding set.
  var noHeadersRange = fullDataRange.offset(
    1, 1,
    fullDataRange.getNumRows() - 1,
    fullDataRange.getNumColumns() - 1);

  if (! noHeadersRange.getBandings()[0]) {
    // The range doesn't already have a banding, so it's
    // safe to apply a new one.
    noHeadersRange.applyRowBanding(
      SpreadsheetApp.BandingTheme.LIGHT_GREY,
      false, false);
  }
  
  // Set a border around all the data, and resize the
  // columns and rows to fit.
  fullDataRange.setBorder(
    true, true, true, true, null, null,
    null,
    SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  sheet.autoResizeColumns(1, fullDataRange.getNumColumns());
  sheet.autoResizeRows(1, fullDataRange.getNumRows());
}

/*
*  Fetch a URL. This will return a response in JSON format.
*/
function fetchData_(url) {
  var response = UrlFetchApp.fetch(url)
  return JSON.parse(response.getContentText());
}

function fillSheetWithData_(resourceDataList, keys, sheet) {
  var numRows = resourceDataList.length;
  var numColumns = keys.length;
  
  var resourceRange = sheet.getRange(1, 1, numRows + 1, numColumns); // +1 since we need the column row. what.
  var resourceValues = resourceRange.getValues(); //2D array, row,column

  // Repopulate resourceValues  
  for (var column = 0; column < numColumns; column++) { //iterate each column
    // First is the column
    var columnHeader = keys[column];
    resourceValues[0][column] = columnHeader;
    
    // Then the rows
    for (var row = 1; row < numRows; row++) {
      var rowObj = resourceDataList[row - 1]; // OBJECT
      var rowValue = rowObj[columnHeader];
      resourceValues[row][column] = rowValue;
    }
  }
  
  sheet.clear();
  resourceRange.setValues(resourceValues);
}

function createNewSheet_(sheetName) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  var sheet = ss.getSheetByName(sheetName);
  // If Sheet Exists, go to that sheet.
  if (sheet) {
    return sheet.activate();
  }
  
  // If not create a new one
  return ss.insertSheet(sheetName);;
}
/*******************************************************************
* File Name : AttendanceExtractor.gs
* Author : Benjamin Reyes
* Description : This is a Google App Script to import the daily
*        attendance to a Monthly Attendance.
* USAGE : The user will be required to create a details sheet
*        which will be used as reference for the monthly and 
*        daily spreadsheet IDs.
*        The user will also need to declare the Google Drive's
*        folder ID as a folder reference.
*/

var details = SpreadsheetApp.openById(<SHEET_DETAILS_ID>);
var details_sheet = details.getSheetByName('details');

function createMonthlySheet() {
  // Get Current Month and Year
  var cur_month = Utilities.formatDate(new Date(), "GMT+8", "MMMM YYYY");

  // Create new Spreadsheet
  var new_monthly_sheet = SpreadsheetApp.create("Attendance Sheet " + cur_month);
  var new_monthly_sheet_id = new_monthly_sheet.getId();
  
  // Add file to Attendance Folder
  var sheet_file = DriveApp.getFileById(new_monthly_sheet_id);
  var cur_folder = DriveApp.getFolderById(<FOLDER_ID>);
  cur_folder.addFile(sheet_file);
  
  //Update sheet ID on sheet details
  details_sheet.getRange(3, 2).setValue(new_monthly_sheet_id);
}

function dailyDump() {
  var dss = SpreadsheetApp.openById(details_sheet.getRange(2, 2).getValue());
  var mss = SpreadsheetApp.openById(details_sheet.getRange(3, 2).getValue());
  
  //Copy Daily Sheet to Monthly Sheet
  var daily_sheet = dss.getSheetByName("daily");
  var copied_sheet = daily_sheet.copyTo(mss);
  copied_sheet.setName(new Date().getDate());
  daily_sheet.clear();
}
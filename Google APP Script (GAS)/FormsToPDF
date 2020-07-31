// Add project trigger.
function afterFormSubmit(e)
{
  const info = e.namedValues;
  const pdfFile = createPDF(info);
  const row = e.range.getRow();
  SpreadsheetApp.getActiveSpreadsheet().getSheetByName('People').getRange(row, 7).setValue(pdfFile.getUrl());
  sendEmail(info['Email Address'][0], pdfFile);
}

//Permissions. run this function
function sendEmail(email, pdfFile)
{
  MailApp.sendEmail(email, 'Attachment example', 'Two files are attached.', {
    name: 'Automatic Emailer Script',
    attachments: [pdfFile]
  });
  
}
function createPDF(info)
{  
  const pdfFolder = DriveApp.getFolderById(PDF_FOLDER_ID);
  const tmpFolder = DriveApp.getFolderById(TMP_FOLDER_ID);
  const templateDoc = DriveApp.getFileById(TEMPLATE_DOC_ID);
  const filename = info['First Name'][0] + info['Last Name'][0];
  //Create new temp file
  const newtmpFile = templateDoc.makeCopy(tmpFolder);
  //Fill up document file.
  const openDoc = DocumentApp.openById(newtmpFile.getId());
  const body = openDoc.getBody();
  body.replaceText("{fn}", info['First Name'][0]);
  body.replaceText("{ln}", info['Last Name'][0]);
  body.replaceText("{qty}", info['Order Quantity'][0]);
  body.replaceText("{addr}", info['Address'][0]);
  openDoc.saveAndClose();

  //Make pdf out of new tmp file
  const blob = newtmpFile.getAs(MimeType.PDF);
  const pdfFile = pdfFolder.createFile(blob).setName(filename);
  tmpFolder.removeFile(newtmpFile);
  return pdfFile;
}

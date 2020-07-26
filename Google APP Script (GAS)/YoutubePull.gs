/*******************************************************************
* File Name : AttendanceExtractor.gs
* Author : Benjamin Reyes
* Description : This is a Google App Script to pull Youtube video
*          details from a search keyword.
*/

function search() {
  var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var results = YouTube.Search.list('id,snippet', {q: "Youtube Income Report", maxResults: 25});
  for(var i in results.items) {
    var item = results.items[i];
    ss.appendRow([item.snippet.title, item.id.videoId, item.snippet.description, item.snippet.thumbnails["default"]["url"]]);
  }
}
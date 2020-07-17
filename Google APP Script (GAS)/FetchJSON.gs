/*******************************************************************
* File Name : FetchJSON.gs
* Author : Benjamin Reyes
* Description : This is a Google Apps Script to fetch Data
*        from a JSON file. This is specifically made for
*        fixer.io REST API.
* Usage: FETCHJSON(<base_url>, <xpath>)
*        API Access key is required, you can get one by signing up 
*        at fixer.io
*/

/**
* Fetch JSON data from given URL
* @param base_url URL of your JSON data as string
* @param xpath JSON node path
* @customfunction
*/
function FETCHJSON(base_url, xpath)
{
  try
  {
    var API_ACCESS_KEY = <ACCESS_KEY>;
    var access_key = "access_key=" + API_ACCESS_KEY;
    var url = base_url + access_key;
    var res = UrlFetchApp.fetch(url);
    var content = res.getContentText();
    
    var json = JSON.parse(content);
    
    var paths = xpath.split("/");
    var pathlength = paths.length;
    for (var i =0 ; i < pathlength; i++)
    {
      json = json[paths[i]];
    }
    
    if(typeof(json) === "undefined") {
      return "Node undefined";
    } else if (typeof(json) === 'object') {
      var tmp = [];
      for (var obj in json) {
        tmp.push([obj, json[obj]]);
      }
      return tmp;
    }
    return json;
  }
  catch(err) {
    return "Error fetching JSON data : \n" + err;
  }
}

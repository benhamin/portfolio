from _gui import GUI
from _utils import Utils
from _constants import Constants

import win32com.client
from os import listdir
import pathlib

if __name__ == "__main__":
  gui = GUI()

  if not gui.file_path.endswith('.xls') and not gui.file_path.endswith('.xlsx') and not gui.file_path.endswith('.xlsm'):
    gui.invalid_selected_file
    print('exit')
    exit()

  sheetname = 'Sheet1'
  xl = win32com.client.DispatchEx('Excel.Application')
  wb = xl.Workbooks.Open(Filename=gui.file_path)
  ws = wb.Sheets(sheetname)

  begin = 1
  end = ws.UsedRange.Rows.Count
  for row in range(begin, end + 1):
    if ws.Range('A{}'.format(row)).Value == 'ORNUMTODELETE':
      ws.Range('A{}'.format(row)).EntireRow.Delete(Shift=-4162) # shift up

  wb.SaveAs(Constants.OUTPUT_FOLDER_DIRECTORY + pathlib.Path(gui.file_path).name)
  wb.Close()
  xl.Quit()
  gui.finished()
  gui.open_output_folder()
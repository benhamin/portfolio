from _utils import Utils
import editpyxl
import locale

class ExcelUtil:
  EXCEL_FILE_INPUT = 'output/PAA_Template.xlsx'
  EXCEL_FILE_OUTPUT = 'output/PAA_Template.xlsx'

  def __init__(self):
    super().__init__()
    self.wb = editpyxl.Workbook()
    self.wb.open(ExcelUtil.EXCEL_FILE_INPUT)
    self.ws = self.wb.active
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

  def write_to_cell(self, cell, value):
    self.ws.cell(cell).value = value

  def save_and_close(self):
    self.wb.save(ExcelUtil.EXCEL_FILE_OUTPUT)
    self.wb.close()
from _utils import Utils

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import os
from io import BytesIO

class PDFExtract:
  def __init__(self):
    super().__init__()
    self.close_files()

  def close_files(self):
    open("convertedText/BasicDetails.txt", "w").close()
    open("convertedText/ProtectionBenefits.txt", "w").close()
    open("convertedText/ProjectedBenefits.txt", "w").close()

  def writelines(self, lines):
    self._checkClosed()
    for line in lines:
       self.write(line)

  #PDF to text Function.
  def pdf_to_text(self, path, page_no):
      manager = PDFResourceManager()
      retstr = BytesIO()
      layout = LAParams(all_texts=True)
      device = TextConverter(manager, retstr, laparams=layout)
      filepath = open(path, 'rb')
      interpreter = PDFPageInterpreter(manager, device)

      fetch_page = 0
      for page in PDFPage.get_pages(filepath, check_extractable=True):
        fetch_page = fetch_page + 1
        if (fetch_page == page_no):
          interpreter.process_page(page)
        else:
          continue

      text = retstr.getvalue()
      filepath.close()
      device.close()
      retstr.close()
      return text

  #open file, add it to list table, then add it to an excel file.
  def getProjectedBenefitsTable(self, age):
    #initialize table
    if age >= 60:
      max_row = 20
    else:
      max_row = 22
    max_col = 8
    table_projected_benefits = [['-' for x in range(max_col)] for x in range(max_row)]
    row_idx = 0
    col_idx = 0
    found = False

    with open("convertedText/ProjectedBenefits.txt", "r", encoding="utf-8") as text_file:
      for lines in text_file:
        if (lines == '\n') or (lines.find('LOW') == 0):
          continue
        if found == False:
          if (lines.find("HIGH (10.00%)*") == 0):
            found = True
          else:
            continue
        else:
          #found what we've been looking for.
          #now we add it to our table list
          lines = lines.replace('\n', '')
          lines = lines.replace(' ', '')
          lines = lines.replace(',', '')
          Utils.print_to_console('input : ' + lines, Utils.LOG_DEBUG)
          if row_idx < max_row:
            Utils.print_to_console('{} , {} \n'.format(row_idx, col_idx), Utils.LOG_DEBUG)
            table_projected_benefits[row_idx][col_idx] = lines
            row_idx = row_idx + 1
          elif col_idx < max_col - 1:
            col_idx = col_idx + 1
            row_idx = 0
            Utils.print_to_console('elif : {} , {} \n'.format(row_idx, col_idx), Utils.LOG_DEBUG)
            table_projected_benefits[row_idx][col_idx] = lines
            row_idx = row_idx + 1
          else:
            break
    return table_projected_benefits

  #open file, add it to list table, then add it to an excel file.
  def getProtectionBenefitsTable(self):
    #initialize table
    d = {
      'Basic' : 0,
      'Disability' : 0,
      'AccidentalDeath' : 0,
      'CriticalIllness' : 0
      }
    found = False

    with open("convertedText/ProtectionBenefits.txt", "r", encoding="utf-8") as text_file:
      for lines in text_file:
        if lines == '\n':
          continue
        if found == False:
          #find this line first.
          #then we put it in our table
          if (lines.find('Protection Benefit') == 0):
            found = True
          else:
            continue
        else:
          lines = lines.replace('\n', '')
          lines = lines.replace(',','')
          try:
            if lines.find(' ') == 0:
              continue
            if (d['Basic'] == 0):
              d['Basic'] = float(lines)
              continue
            if (d['Disability'] == 0):
              d['Disability'] = float(lines)
              continue
            if (d['AccidentalDeath'] == 0):
              d['AccidentalDeath'] = float(lines)
              continue
            if (d['CriticalIllness'] == 0):
              d['CriticalIllness'] = float(lines)
              return d
          except:
            continue
    return d

  def getBasicDetails(self):
    foundAge = False
    age = 0
    max_row = 3
    max_col = 2
    table_basic_details = [['-' for x in range(max_col)] for x in range(max_row)]
    row_idx = 0
    col_idx = 0
    table_basic_details[0][0] = 'Age'
    table_basic_details[1][0] = 'Total Annual Premium'
    with open("convertedText/BasicDetails.txt", "r", encoding="utf-8") as text_file:
      for lines in text_file:
        if lines == '\n' or lines == ':\n':
          continue
        if foundAge == False:
          if (lines.find('Age') == 0):
            foundAge = True
            continue
          else:
            continue
        else:
          #check if line is an integer, if not continue
          lines = lines.replace('\n', '')
          lines = lines.replace(' ', '')
          lines = lines.replace('PhP', '')
          lines = lines.replace(',', '')
          if (age == 0):
            try:
              age = int(lines)
              table_basic_details[0][1] = age
              continue
            except:
              continue
          else:
            try:
              table_basic_details[1][1] = int(lines)
              return table_basic_details
            except:
              Utils.print_to_console("Something's off", Utils.LOG_DEBUG)
              continue

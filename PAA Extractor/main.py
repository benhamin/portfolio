from _utils import Utils
from _pdfextract import PDFExtract
from _constants import Constants
from _excelUtil import ExcelUtil
from _gui import GUI

import os
import locale

if __name__ == "__main__":
  Utils.set_debug_level(Utils.LOG_WARNING)

  pdfextract = PDFExtract()
  gui = GUI()

  Utils.print_to_console(gui.file_path, Utils.LOG_DEBUG)

  #Convert pdf to text.
  #Basic Details
  extracted_text = pdfextract.pdf_to_text(gui.file_path, 1)
  decoded_text = extracted_text.decode("utf-8")
  with open("convertedText/BasicDetails.txt", "a", encoding="utf-8") as text_file:
    text_file.writelines(decoded_text)

  #Protection Benefits
  extracted_text = pdfextract.pdf_to_text(gui.file_path, 2)
  decoded_text = extracted_text.decode("utf-8")
  with open("convertedText/ProtectionBenefits.txt", "a", encoding="utf-8") as text_file:
    text_file.writelines(decoded_text)

  #Projected Benefits
  extracted_text = pdfextract.pdf_to_text(gui.file_path, 3)
  decoded_text = extracted_text.decode("utf-8")
  with open("convertedText/ProjectedBenefits.txt", "a", encoding="utf-8") as text_file:
    text_file.writelines(decoded_text)

  basic_details_table = pdfextract.getBasicDetails()
  age = basic_details_table[0][1]
  Utils.print_to_console('Client\'s Age : {}'.format(age), Utils.LOG_WARNING)

  projected_benefits_table = pdfextract.getProjectedBenefitsTable(age)
  Utils.print_to_console(projected_benefits_table, Utils.LOG_DEBUG)

  protection_benefits = pdfextract.getProtectionBenefitsTable()

  excel_util = ExcelUtil()

  monthly_premium = basic_details_table[1][1]/12
  death_benefit = Utils.to_million_notation(protection_benefits['Basic'])
  disability_benefit = Utils.to_million_notation(protection_benefits['Disability'])
  critical_illness_benefit = Utils.to_million_notation(protection_benefits['CriticalIllness'])
  accidental_death_benefit = Utils.to_million_notation(protection_benefits['AccidentalDeath'])
  retirement_benefit = Utils.to_million_notation(projected_benefits_table[19][7])

  excel_util.write_to_cell(Constants.CELLS['MONTHLY_PREMIUM'], monthly_premium)
  excel_util.write_to_cell(Constants.CELLS['DEATH_BENEFIT'], death_benefit)
  excel_util.write_to_cell(Constants.CELLS['DISABILITY_BENEFIT'], disability_benefit)
  excel_util.write_to_cell(Constants.CELLS['CRITICAL_ILLNESS_BENEFIT'], critical_illness_benefit)
  excel_util.write_to_cell(Constants.CELLS['ACCIDENTAL_DEATH_BENEFIT'], accidental_death_benefit)
  excel_util.write_to_cell(Constants.CELLS['RETIREMENT_BENEFIT'], retirement_benefit)

  Utils.print_to_console('Monthly Premium : {}'.format(monthly_premium), Utils.LOG_WARNING)
  Utils.print_to_console('Death Benefit : {}'.format(death_benefit), Utils.LOG_WARNING)
  Utils.print_to_console('Disability Benefit : {}'.format(disability_benefit), Utils.LOG_WARNING)
  Utils.print_to_console('Critical Illness Benefit : {}'.format(critical_illness_benefit), Utils.LOG_WARNING)
  Utils.print_to_console('Accidental Death Benefit : {}'.format(accidental_death_benefit), Utils.LOG_WARNING)
  Utils.print_to_console('Retirement Benefit : {}'.format(retirement_benefit), Utils.LOG_WARNING)

  #Fillup the ages and projected benefits in increments of 5
  for i in range(1, 5):
    cell = 'AGE_' + str(i)
    age = locale.atoi(projected_benefits_table[5 * i - 1][1])
    excel_util.write_to_cell(Constants.CELLS[cell], age)
    Utils.print_to_console('Age : {}'.format(age), Utils.LOG_WARNING)

    cell = 'PROJECTED_BENEFITS_' + str(i)
    projected_benefit = locale.atof(projected_benefits_table[5 * i - 1][-1])
    excel_util.write_to_cell(Constants.CELLS[cell], projected_benefit)
    Utils.print_to_console('Projection : {}'.format(projected_benefit), Utils.LOG_WARNING)
  excel_util.save_and_close()
  gui.finished()
  gui.open_output_folder()
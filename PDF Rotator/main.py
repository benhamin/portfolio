from _gui import GUI
from _utils import Utils
from _constants import Constants

from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
import pathlib

if __name__ == "__main__":
  gui = GUI()
  print(gui.file_path)
  if not gui.file_path.endswith('.pdf'):
    gui.invalid_selected_file
    exit()

  pdf_input = open(gui.file_path, 'rb')
  pdf_reader = PdfFileReader(pdf_input)
  pdf_writer = PdfFileWriter()
  for pagenum in range(pdf_reader.numPages):
      page = pdf_reader.getPage(pagenum)
      page.rotateClockwise(270)
      pdf_writer.addPage(page)
  Utils.print_to_console(Constants.OUTPUT_FOLDER_DIRECTORY, Utils.LOG_WARNING)
  pdf_out = open(Constants.OUTPUT_FOLDER_DIRECTORY + pathlib.Path(gui.file_path).name, 'wb')
  pdf_writer.write(pdf_out)
  pdf_out.close()
  pdf_input.close()
  gui.finished()
  gui.open_output_folder()
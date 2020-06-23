#
# Description : This simple script splits a pdf page and merges it
#

from PyPDF2 import PdfFileWriter, PdfFileReader

def split_and_merge(input_file, output_file_name):
  with open(input_file, "rb") as _file:
      input1 = PdfFileReader(_file)
      input2 = PdfFileReader(_file)
      output = PdfFileWriter()
      numPages = input1.getNumPages()

      for i in range(numPages):
        page = input1.getPage(i)
        page2 = input2.getPage(i)

        upper_right = page.cropBox.getUpperRight()

        init_node = upper_right[0]
        end_node = upper_right[1]

        page.cropBox.lowerLeft = (0, 0)
        page.cropBox.upperRight = (init_node/2, end_node)
        output.addPage(page)

        page2.cropBox.lowerLeft = (init_node/2, 0)
        page2.cropBox.upperRight = (init_node, end_node)
        output.addPage(page2)

      with open(output_file_name + ".pdf", "wb") as _out_file:
          output.write(_out_file)

# Sample Usage
# This will create an output.pdf file on the same directory
split_and_merge("example_input.pdf", "output")
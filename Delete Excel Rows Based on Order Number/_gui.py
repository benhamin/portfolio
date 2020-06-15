from _utils import Utils
from _constants import Constants
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os

class GUI:
  def __init__(self):
    super().__init__()
    self.root = tk.Tk()
    self.root.title('{} {}'.format(Constants.APP_NAME, Constants.APP_VERSION))
    self.root.withdraw()
    self.browse_file()

  def browse_file(self):
    FILEOPENOPTIONS = dict(defaultextension = ".xlsx", initialdir = Constants.ROOT_DIRECTORY,
      filetypes=[('Excel File', '*.xlsx')])
    self.file_path = fd.askopenfilename(**FILEOPENOPTIONS)

  def finished(self):
    mb.showinfo(Constants.APP_NAME, "Processing Done! Opening Folder")

  def invalid_selected_file(self):
    mb.showinfo(Constants.APP_NAME, "Invalid Selected File!")

  def open_output_folder(self):
    real_path = os.path.realpath(Constants.OUTPUT_FOLDER_DIRECTORY)
    os.startfile(real_path)
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
    self.root.title('PAA Extractor {}'.format(Constants.APP_VERSION))
    self.root.withdraw()
    self.browse_file()

  def browse_file(self):
    FILEOPENOPTIONS = dict(defaultextension = ".pdf", initialdir = Constants.ROOT_DIRECTORY,
      filetypes=[('PDF File', '*.pdf')])
    self.file_path = fd.askopenfilename(**FILEOPENOPTIONS)

  def finished(self):
    mb.showinfo("Wala na...", "Finish na...")

  def open_output_folder(self):
    real_path = os.path.realpath(Constants.OUTPUT_FOLDER_DIRECTORY)
    os.startfile(real_path)
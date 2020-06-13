import os

class Constants:
  """This  class holds the constants for PAA Extractor tool"""

  APP_VERSION = 'v1.0'
  ROOT_DIRECTORY = os.getcwd()
  OUTPUT_FOLDER_DIRECTORY = ROOT_DIRECTORY + '\\output\\'

  # CELLS represents the Excel Cell that the tool will fill-up.
  # If in case the Excel Template changed, assign appropriate cell here.

  CELLS = {
    'DEATH_BENEFIT': 'C10',
    'DISABILITY_BENEFIT': 'C11',
    'CRITICAL_ILLNESS_BENEFIT': 'C12',
    'ACCIDENTAL_DEATH_BENEFIT': 'C20',
    'RETIREMENT_BENEFIT': 'C24',

    'AGE_1' : 'H11',
    'AGE_2' : 'H12',
    'AGE_3' : 'H13',
    'AGE_4' : 'H14',

    'PROJECTED_BENEFITS_1' : 'I11',
    'PROJECTED_BENEFITS_2' : 'I12',
    'PROJECTED_BENEFITS_3' : 'I13',
    'PROJECTED_BENEFITS_4' : 'I14',

    'MONTHLY_PREMIUM' : 'F8'
  }
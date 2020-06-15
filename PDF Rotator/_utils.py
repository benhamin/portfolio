from pprint import pprint

class Utils:
  LOG_DEBUG = 1
  LOG_WARNING = 2
  LOG_ERROR = 3
  DEBUG_LEVEL = LOG_WARNING

  @staticmethod
  def set_debug_level(level):
    Utils.DEBUG_LEVEL = level

  @staticmethod
  def print_to_console(text, level):
    if level >= Utils.DEBUG_LEVEL: #make this false
      pprint(text)
    else:
      pass
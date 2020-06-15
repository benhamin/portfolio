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
    if level >= Utils.DEBUG_LEVEL:
      pprint(text)
    else:
      pass

  @staticmethod
  def to_million_notation(value):
    Utils.print_to_console(value, Utils.LOG_DEBUG)
    value = float(value)
    return '{}{}'.format(str(round(value/1000000, 1)),str('M'))
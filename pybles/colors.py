class Colors(object):

  HEADER = '\033[95m'
  OKBLUE = '\033[47m\033[1;30m'
  OKGREEN = '\033[42m\033[1;37m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

  RED = '\033[31m'
  STRONG_RED = '\033[1;31m'
  GREEN = '\033[32m'
  STRONG_GREEN = '\033[1;32m'
  BLUE = '\033[34m'
  STRONG_BLUE = '\033[1;34m'
  PURPLE = '\033[35m'
  STRONG_PURPLE = '\033[1;35m'
  TURQUESA = '\033[36m'
  STRONG_TURQUESA = '\033[1;36m'
  WHITE = '\033[37m'
  STRONG_WHITE = '\033[1;37m'
  YELLOW = '\033[38m'
  STRONG_YELLOW = '\033[1;38m'

  #BACKGROUNDS
  BG_GRAY = '\033[40m'
  BG_RED = '\033[41m'
  BG_GREEN = '\033[42m'
  BG_YELLOW = '\033[43m'
  BG_BLUE = '\033[44m'
  BG_PURPLE = '\033[45m'
  BG_TURQUESA = '\033[46m'
  BG_WHITE = '\033[47m'
  BG_BLACK = '\033[48m'

  def __init__(self):
    self.header = None
    self.cell = None
    self.bg_header = ""
    self.bg_cell = ""

    self.color_names = {'OKBLUE': self.OKBLUE,
                        'OKGREEN': self.OKGREEN,
                        'WARNING': self.WARNING,
                        'FAIL': self.FAIL,
                        'HEADER': self.HEADER,
                        'RED': self.RED,
                        'STRONG_RED': self.STRONG_RED,
                        'GREEN': self.GREEN,
                        'STRONG_GREEN': self.STRONG_GREEN,
                        'BLUE': self.BLUE,
                        'STRONG_BLUE': self.STRONG_BLUE,
                        'PURPLE': self.PURPLE,
                        'STRONG_PURPLE': self.STRONG_PURPLE,
                        'TURQUESA': self.TURQUESA,
                        'STRONG_TURQUESA': self.STRONG_TURQUESA,
                        'WHITE': self.WHITE,
                        'STRONG_WHITE': self.STRONG_WHITE,
                        'YELLOW': self.YELLOW,
                        'STRONG_YELLOW': self.STRONG_YELLOW,
                        'BG_GRAY': self.BG_GRAY,
                        'BG_RED': self.BG_RED,
                        'BG_GREEN': self.BG_GREEN,
                        'BG_YELLOW': self.BG_YELLOW,
                        'BG_BLUE': self.BG_BLUE,
                        'BG_PURPLE': self.BG_PURPLE,
                        'BG_TURQUESA': self.BG_TURQUESA,
                        'BG_WHITE': self.BG_WHITE,
                        'BG_BLACK': self.BG_BLACK, }

  def set_header_color(self, name):
    try:
      self.header = self.color_names[name]
    except:
      self.header = self.HEADER

  def set_cell_color(self, name):
    try:
      self.cell = self.color_names[name]
    except:
      self.cell = self.OKBLUE

  def set_header_background_color(self, name):
    try:
      self.bg_header = self.color_names[name]
    except:
      self.bg_header = None

  def set_cell_background_color(self, name):
    try:
      self.bg_cell = self.color_names[name]
    except:
      self.bg_cell = None

  def get_header_color(self):
    if self.header is None:
      return self.HEADER

    return self.header

  def get_cell_color(self):
    if self.cell is None:
      return self.OKBLUE

    return self.cell

  def get_header_background_color(self):
    return self.bg_header

  def get_cell_background_color(self):
    return self.bg_cell

  def get_sample(self):
    for color in self.color_names:
      print "%s%s%s" % (self.color_names[color], color, self.ENDC)


if __name__ == '__main__':
  cc = Colors()
  cc.get_sample()
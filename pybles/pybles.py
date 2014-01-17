#!/usr/bin/env python
from blessings import Terminal
from colors import Colors

import json

class IncorrectNumberOfCells(Exception):

  def __str__(self):
    return "The amount of cells is icorrect"


class HeaderAlreadySet(Exception):

  def __str__(self):
    return "The number of columns can't be modified once a line has been added"


class Pyble(object):

  def __init__(self, row_token=None, column_token=None, 
              header_color='STRONG_YELLOW', header_background_color='BG_BLUE',
              cell_a_color='STRONG_BLUE', cell_b_color='STRONG_YELLOW',
              cell_a_background_color='BG_YELLOW', cell_b_background_color='BG_BLUE'):
  
    self.table        = list()
    self.header       = list()
    self.lines        = list()
    self.longest      = 0
    self.row_token    = '-'
    self.column_token = '|'

    self.c = Colors()
    self.c.set_header_color(header_color)
    self.c.set_header_background_color(header_background_color)
    self.c.set_cell_a_color(header_color)
    self.c.set_cell_b_color(header_color)
    self.c.set_cell_a_background_color(header_color)
    self.c.set_cell_b_background_color(header_color)

    self.color = False

    if row_token != None:
      self.row_token = row_token[0]

    if column_token != None:
      self.column_token = column_token[0]

  def __str__(self):
    self.get_table_info()

  def get_color(self):
    return self.color

  def set_color(self, color):
    self.color = color

  def add_column(self, title):
    if len(self.lines) == 0:
      self.header.append(title) 
    else:
      raise HeaderAlreadySet

  def add_line(self, line):
    if len(line) == self.__get_columns_count():
      self.lines.append(line)
    else:
      raise IncorrectNumberOfCells

  def __get_columns_count(self):
    return len(self.header)

  def __configure_length(self, old_header, old_lines):
    header = list()
    lines  = list()

    for cell in old_header:
      header.append( {'name': cell, 'len': len(cell)} )

    for line in old_lines:
      tmp_line = list()
      for cell in line:
        try:
          tmp_line.append( {'name': cell, 'len': len(cell)} )
        except TypeError:
          tmp_line.append( {'name': cell, 'len': len(str(cell))} )

      lines.append(tmp_line)

    return header, lines

  def __set_column_length(self, header, lines):
    for cellnumber in range(len(header)):
      for line in lines:
        if header[cellnumber]['len'] < line[cellnumber]['len']:
          header[cellnumber]['len'] = line[cellnumber]['len']

    for cellnumber in range(len(header)):
      for line in lines:
        line[cellnumber]['len'] = header[cellnumber]['len']        

    return header, lines

  def __show_dots(self, header):
    dots = 0
    for cell in header:
      dots += cell['len']

    dots = self.row_token * (dots + (3 * len(header)) + 1)

    print dots

  def __show_header(self, header):
    t = Terminal()
    header_as_string = self.column_token

    self.__show_dots(header)

    for cell in header:
      if self.color:
        header_as_string += " %s%s%s%s%s %s" % (self.c.get_header_background_color(), self.c.get_header_color(), cell['name'].upper(), " " * (cell['len'] - len(cell['name'])), self.c.ENDC, self.column_token)
      else:
        header_as_string += " %s%s %s" % (cell['name'].upper(), " " * (cell['len'] - len(cell['name'])), self.column_token)

    print header_as_string

    self.__show_dots(header)

  def __show_lines(self, lines, header, highlight=None):
    lines_as_string = ""
    t = Terminal()
    color = 0

    for line in lines:
      lines_as_string += self.column_token
      for cell in line:
        try:
          name = cell['name']
          if highlight in name:
            name = "%s" % t.bold_black_on_yellow(name)

          lines_as_string += " %s%s %s" % (name, " " * (cell['len'] - len(cell['name'])), self.column_token)
        except TypeError:
          if self.color:
            if color == 1:
              lines_as_string += " %s%s%s%s %s" % (self.c.OKBLUE, name, " " * (cell['len'] - len(str(cell['name']))), self.c.ENDC, self.column_token)
            else:
              lines_as_string += " %s%s%s%s %s" % (self.c.OKGREEN, name, " " * (cell['len'] - len(str(cell['name']))), self.c.ENDC, self.column_token)
              #lines_as_string += " %s%s %s" % (name, " " * (cell['len'] - len(str(cell['name']))), self.column_token)
          else:
            lines_as_string += " %s%s %s" % (name, " " * (cell['len'] - len(str(cell['name']))), self.column_token)

      if self.color:
        if color == 0:
          color = 1
        else:
          color = 0

      lines_as_string += "\n"

    print lines_as_string.strip("\n") 
    self.__show_dots(header)

  def get_table_as_json(self):
    header, lines = self.__configure_length(self.header, self.lines)
    header, lines = self.__set_column_length(header, lines)

    table = {}
    table['header'] = header
    table['rows'] = lines

    return json.dumps(table)

  def get_table_info(self):
    print "Table information"
    print "Columns count: %s" % len(self.header)
    print "Rows count: %s" % len(self.lines)

  def show_table(self, highlight=None):
    header, lines = self.__configure_length(self.header, self.lines)
    header, lines = self.__set_column_length(header, lines)

    if len(header) != 0:
      self.__show_header(header)

    if len(lines) != 0:
      self.__show_lines(lines, header, highlight)

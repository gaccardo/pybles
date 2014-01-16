class IncorrectNumberOfCells(Exception):

  def __str__(self):
    return "La cantidad de celdas es incorrecta"


class HeaderAlreadySet(Exception):

  def __str__(self):
    return "El numero de columnas no puede ser modificado una vez seteadas filas"
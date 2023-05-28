#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


for row in sys.stdin:
  row_separada=row.split(",")
  print(row_separada[2])
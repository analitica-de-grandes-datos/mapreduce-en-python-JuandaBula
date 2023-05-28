#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  row_separada=row.split("   ")
  sys.stdout.write(row_separada[1][5:7]+"\n")
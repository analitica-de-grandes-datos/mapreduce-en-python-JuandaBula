#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dictionary = {}

for row in sys.stdin:
    row_separada=row.split(",")
    if   row_separada[0] in dictionary.keys():
        if dictionary[row_separada[0]] < int(row_separada[1]):
            dictionary[row_separada[0]] = int(row_separada[1])
    else:
        dictionary[row_separada[0]] = int(row_separada[1])

for key in dictionary.keys():
  key_edit=key.strip()
  string_valor=str(dictionary[key])
  print(key_edit  + "\t" + string_valor)
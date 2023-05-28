#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list=[]

for row in sys.stdin:
    row_separada=row.split(",")
    list.append((row_separada[0],row_separada[1],int(row_separada[2])))
    list.sort(key=lambda x: x[2])
    list.sort(key=lambda x: x[0])


for key in list:
  sys.stdout.write(key[0] + "   " + key[1]+ "   " + str(key[2])+"\n")
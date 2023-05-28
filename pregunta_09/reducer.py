#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list=[]

for row in sys.stdin:
    row_separada=row.split(",")
    list.append((row_separada[0],row_separada[1],int(row_separada[2])))
    list.sort(key=lambda x: x[2])
 
for registro in list[0:6]:
  sys.stdout.write(registro[0] + "   " + registro[1]+ "   " + str(registro[2])+"\n")
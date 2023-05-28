#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dictionary={}

for row in sys.stdin:
    row_separada=row.split(";")
    numero=int(row_separada[0])
    row_separada[1]=row_separada[1].strip()
    claves=row_separada[1].split(",")
    for clave in claves:
       clave=str(clave.replace(" ",""))
       if clave in dictionary.keys():
          dictionary[clave].append(numero)
          dictionary[clave].sort()
       else:
          dictionary[clave]=[numero]

dictionary_ordenado = {}
llaves_ordenadas = sorted(dictionary)
for key in llaves_ordenadas:
  dictionary_ordenado[key] = dictionary[key]
 
for clave in dictionary_ordenado.keys():
    sys.stdout.write(clave + "\t" + str(dictionary_ordenado[clave])[1:-1].replace(" ","")+"\n")


# run with python3 test.py
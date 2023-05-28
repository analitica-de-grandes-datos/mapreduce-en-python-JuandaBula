#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dict_count = {}
dict_sum={}

for row in sys.stdin:
  row_separada=row.split(",")
  if row_separada[0] in dict_count.keys():
    dict_count[row_separada[0]] += 1
    dict_sum[row_separada[0]]+=int(row_separada[1])
  else:
    dict_count[row_separada[0]] = 1
    dict_sum[row_separada[0]]=int(row_separada[1])
    
for key in dict_count.keys():
  suma=str(float(dict_sum[key]))
  promedio=str(dict_sum[key]/dict_count[key])
  sys.stdout.write(key+"\t"+suma+"\t"+promedio+"\n")
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dict_count = {}

for letter in sys.stdin:
  if letter in dict_count.keys():
    dict_count[letter] += 1
  else:
    dict_count[letter] = 1
    
for key in dict_count.keys(): 
  print(key.replace("\n","") + ","+str(dict_count[key]))
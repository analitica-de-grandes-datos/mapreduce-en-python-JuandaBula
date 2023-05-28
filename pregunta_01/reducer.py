#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count_dictionary = {}

for credit_history in sys.stdin:
  if credit_history in count_dictionary.keys():
    count_dictionary[credit_history] += 1
  else:
    count_dictionary[credit_history] = 1
    
for key in count_dictionary.keys():
  key_edit=key.strip()
  string_valor=str(count_dictionary[key])
  print(key_edit  + "\t" + string_valor)  


  # correr con: $ cat credit.csv | python3 mapper.py | sort | python3 reducer.py
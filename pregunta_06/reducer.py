#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# dict_min = {}
# dict_max = {}

# for row in sys.stdin:
#     row=row.split(",")
#     if row[0] in dict_min:
#         if dict_min[row[0]]>row[1]:
#             dict_min[row[0]]=row[1]
#         elif dict_max[row[0]]<row[1]:
#             dict_max[row[0]]=row[1]
#     else:
#         dict_min[row[0]]=row[1]
#         dict_max[row[0]]=row[1]
        
# for key in dict_max.keys():
#   key_edit=key.strip()
#   string_max=str(dict_max[key])
#   string_min=str(dict_min[key])
#   print(key_edit.replace("\n","")  + "\t" + string_max.replace("\n","")+ "\t" + string_min.replace("\n","")) 




if __name__ == "__main__":
    atrib = {}
    for row in sys.stdin:
        columns = row.split(",")
        if len(columns) == 2:
            letter = columns[0]
            amount = float(columns[1])
            if letter in atrib:
                atrib[letter] = {
                    'max': max(atrib[letter]['max'], amount),
                    'min': min(atrib[letter]['min'], amount)
                }
            else:
                atrib[letter] = {'max': amount, 'min': amount}
    
    atrib_sort = sorted(atrib.items(), key=lambda x: x[0])
    for atrib, value in atrib_sort:
        sys.stdout.write(f"{atrib}\t{value['max']}\t{value['min']}\n")
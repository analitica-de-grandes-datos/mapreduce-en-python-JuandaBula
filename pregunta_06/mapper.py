#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# for row in sys.stdin:
#   row_separada=row.split("   ")
#   sys.stdout.write(row_separada[0]+","+row_separada[2])


if __name__ == "__main__":
    for row in sys.stdin:
        columnas = row.split("   ")
        letra = columnas[0]
        valor = columnas[2]
        sys.stdout.write(f"{letra},{valor}\n")
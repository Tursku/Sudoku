from randomSudokuFormatter import run_RandomFormatter

f = open("Sudoku/Sudoku.txt", "r")
Sudoku = f.read()
lista = []

for x in Sudoku:
    if x == '[':
        pass
    elif x == ']':
        pass
    elif x == ',':
        pass
    elif x == "\n":
        pass
    else:
        x = int(x)
        lista.append(x)

chunked_list = list()
chunk_size = 9
for i in range(0, len(lista), chunk_size):
    chunked_list.append(lista[i:i+chunk_size])


run_RandomFormatter(lista)
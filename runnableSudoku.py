from randomSudoku import run_RandomSudoku
from sudokuSolver import run_SudokuSolver
from randomSudokuFormatter import run_RandomFormatter

lista = []
run_RandomSudoku()
print("\n Random sudoku : \n")
f = open("Sudoku/Sudoku.txt", "r")
Sudoku = f.read()

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
        
run_RandomFormatter(lista)

jaettuLista = list()
jako = 9
for i in range(0, len(lista), jako):
    jaettuLista.append(lista[i:i + jako])
print("")
kysymys = input("Näytä vastaus (Enter)")

print("\n Ratkaistu sudoku : \n")

run_SudokuSolver(jaettuLista)








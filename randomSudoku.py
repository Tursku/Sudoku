# -*- coding: utf-8 -*-
def run_RandomSudoku():

    from random import sample

    pohja  = 3
    sivu  = pohja*pohja

    def pattern(r,c): 
        return (pohja*(r%pohja)+r//pohja+c)%sivu


    def shuffle(s): 
        return sample(s,len(s))

    rangePohja = range(pohja) 

    rivit = [ g*pohja + r for g in shuffle(rangePohja) for r in shuffle(rangePohja) ] 
    sarake = [ g*pohja+ c for g in shuffle(rangePohja) for c in shuffle(rangePohja) ]

    numerot = shuffle(range(1,pohja*pohja+1))
    pelilauta = [ [numerot[pattern(r,c)] for c in sarake] for r in rivit ]

    neliöt = sivu*sivu
    tyhjä = neliöt * 2//5        # vaikeustaso

    for p in sample(range(neliöt),tyhjä):
        pelilauta[p//sivu][p%sivu] = 0

    numero = len(str(sivu))
    open('Sudoku.txt', 'w').close() # Empties the file
    y = 0
    for line in pelilauta: 
        y += 1

        if y == 9:  # Ei printtaa rivivaihtoa viimiseen
            valmisSudoku = ("["+",".join(f"{n or '0':{numero}}" for n in line)+"]")
            file = open("Sudoku.txt","a")
            file.write(valmisSudoku)

        else:
            valmisSudoku = ("["+",".join(f"{n or '0':{numero}}" for n in line)+"]")
            file = open("Sudoku.txt","a")
            file.write(valmisSudoku + '\n')

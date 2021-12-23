def run_RandomSudoku():

    from random import sample

    base  = 3
    side  = base*base

    def pattern(r,c): 
        return (base*(r%base)+r//base+c)%side


    def shuffle(s): 
        return sample(s,len(s))

    rBase = range(base) 

    rows = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]

    nums = shuffle(range(1,base*base+1))
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    squares = side*side
    empties = squares * 3//5        # vaikeustaso

    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    numSize = len(str(side))
    open('Sudoku/Sudoku.txt', 'w').close() # Empties the file
    y = 0
    for line in board: 
        y += 1

        if y == 9:  # Ei printtaa rivivaihtoa viimiseen
            completedSudoku = ("["+",".join(f"{n or '0':{numSize}}" for n in line)+"]")
            file = open("Sudoku/Sudoku.txt","a")
            file.write(completedSudoku)

        else:
            completedSudoku = ("["+",".join(f"{n or '0':{numSize}}" for n in line)+"]")
            file = open("Sudoku/Sudoku.txt","a")
            file.write(completedSudoku + '\n')

# -*- coding: utf-8 -*-
import sys
from copy import deepcopy

def run_SudokuSolver(Sudoku):

    def output(a):
        sys.stdout.write(str(a))
    def print_field(Sudoku):
        if not Sudoku:
            output("Ei voi ratkaista")
            return

        for i in range(9):
            for j in range(9):
                solu = Sudoku[i][j]
                if solu == 0 or isinstance(solu, set):
                    output('.')
                else:
                    output(solu)
                if (j + 1) % 3 == 0 and j < 8:
                    output(' |')

                if j != 8:
                    output(' ')
            output('\n')
            if (i + 1) % 3 == 0 and i < 8:
                output("- - - + - - - + - - -\n")

    def read(Sudoku):
        state = deepcopy(Sudoku)
        for i in range(9):
            for j in range(9):
                solu = state[i][j]
                if solu == 0:
                    state[i][j] = set(range(1,10))
        return state
    state = read(Sudoku)


    def done(state): # Check onko valmis
        for rivi in state:
            for solu in rivi:
                if isinstance(solu, set):
                    return False
        return True

    def propagate_step(state):
        uudetLuvut = False

        # vaakarivien sääntö
        for i in range(9):
            rivi = state[i]
            arvot = set([x for x in rivi if not isinstance(x, set)])
            for j in range(9):
                if isinstance(state[i][j], set):
                    state[i][j] -= arvot
                    if len(state[i][j]) == 1:
                        val = state[i][j].pop()
                        state[i][j] = val
                        arvot.add(val)
                        uudetLuvut = True
                    elif len(state[i][j]) == 0:
                        return False, None

        # pystyrivien sääntö
        for j in range(9):
            sarake = [state[x][j] for x in range(9)]
            arvot = set([x for x in sarake if not isinstance(x, set)])
            for i in range(9):
                if isinstance(state[i][j], set):
                    state[i][j] -= arvot
                    if len(state[i][j]) == 1:
                        val = state[i][j].pop()
                        state[i][j] = val
                        arvot.add(val)
                        uudetLuvut = True
                    elif len(state[i][j]) == 0:
                        return False, None

        # 3x3 neliön sääntö
        for x in range(3):
            for y in range(3):
                arvot = set()
                for i in range(3 * x, 3 * x + 3):
                    for j in range(3 * y, 3 * y + 3):
                        solu = state[i][j]
                        if not isinstance(solu, set):
                            arvot.add(solu)
                for i in range(3 * x, 3 * x + 3):
                    for j in range(3 * y, 3 * y + 3):
                        if isinstance(state[i][j], set):
                            state[i][j] -= arvot
                            if len(state[i][j]) == 1:
                                val = state[i][j].pop()
                                state[i][j] = val
                                arvot.add(val)
                                uudetLuvut = True
                            elif len(state[i][j]) == 0:
                                return False, None
        return True, uudetLuvut

    def propagate(state):
        while True:
            voikoRatkaista, uusiLuku = propagate_step(state)
            if not voikoRatkaista:
                return False
            if not uusiLuku:
                return True

    def solve(state):
        voikoRatkaista = propagate(state)

        if not voikoRatkaista:
            return None

        if done(state):
            return state

        for i in range(9):
            for j in range(9):
                solu = state[i][j]
                if isinstance(solu, set):
                    for value in solu:
                        new_state = deepcopy(state)
                        new_state[i][j] = value
                        ratkaistu = solve(new_state)
                        if ratkaistu is not None:
                            return ratkaustu
                    return None

    print_field(solve(state))
    print("")




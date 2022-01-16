# -*- coding: utf-8 -*-
def run_RandomFormatter(Sudoku):
    rivi1 = ""
    rivi2 = ""
    rivi3 = ""
    rivi4 = ""
    rivi5 = ""
    rivi6 = ""
    rivi7 = ""
    rivi8 = ""
    rivi9 = ""
    y = 0
    välipala = ("- - - + - - - + - - -")

    for x in Sudoku:
        
        y +=1
        if y <=9:
            if y %3==0 and y < 9:
                rivi1 = rivi1 + str(x) + " " + "|" + " "
            else:
                rivi1 = rivi1 + str(x) + " "
        
        elif y <=18:
            if y %3==0 and y < 18:
                rivi2 = rivi2 + str(x) + " " + "|" + " "
            else:
                rivi2 = rivi2 + str(x) + " "

        elif y <=27:
            if y %3==0 and y < 27:
                rivi3 = rivi3 + str(x) + " " + "|" + " "
            else:
                rivi3 = rivi3 + str(x) + " "

        elif y <=36:
            if y %3==0 and y < 36:
                rivi4 = rivi4 + str(x) + " " + "|" + " "
            else:
                rivi4 = rivi4 + str(x) + " "

        elif y <=45:
            if y %3==0 and y < 45:
                rivi5 = rivi5 + str(x) + " " + "|" + " "
            else:
                rivi5 = rivi5 + str(x) + " "

        elif y <=54:
            if y %3==0 and y < 54:
                rivi6 = rivi6 + str(x) + " " + "|" + " "
            else:
                rivi6 = rivi6 + str(x) + " "

        elif y <=63:
            if y %3==0 and y < 63:
                rivi7 = rivi7 + str(x) + " " + "|" + " "
            else:
                rivi7 = rivi7 + str(x) + " "

        elif y <=72:
            if y %3==0 and y < 72:
                rivi8 = rivi8 + str(x) + " " + "|" + " "
            else:
                rivi8 = rivi8 + str(x) + " "

        elif y <=81:
            if y %3==0 and y < 81:
                rivi9 = rivi9 + str(x) + " " + "|" + " "
            else:
                rivi9 = rivi9 + str(x) + " "

       
    print(rivi1)
    print(rivi2)
    print(rivi3)
    print(välipala)
    print(rivi4)
    print(rivi5)
    print(rivi6)
    print(välipala)
    print(rivi7)
    print(rivi8)
    print(rivi9)

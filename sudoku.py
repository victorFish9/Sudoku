# tee ratkaisu tänne
def tulosta(sudoku: list):
    b = 0
    c = 0
    while True:
        for x in sudoku:
            b += 1
            for a in x:
                c += 1
                if c > 2:
                    if a > 0:
                        print(f"{a} ", end=" ")
                    else:
                        print("_ ", end=" ")
                    c = 0
                else:
                    if a > 0:
                        #c += 1
                        print(f"{a} ", end="")
                        #print(" ")
                    else:
                        #c += 1
                        print("_ ", end="")
            if b > 2:
                print()
                b = 0
            print()
        break

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku[rivi_nro][sarake_nro] = luku

def sudoku_oikein(sudoku: list):
    l = []
    rn = 0
    snStart = 0
    snEnd = 3
    rnStart = 0
    rnEnd = 3
    answer = True
    a = 0
    stopPoint = 0
    while a <= 9:
        if answer == False:
            break
        else:
            for x in sudoku[rnStart:rnEnd]:
                for a in x[snStart:snEnd]:
                    l.append(a)
            
            
            if len(l) == 9:
                l = [i for i in l if i != 0]
                if len(l) != len(set(l)):
                    answer = False
                    l.clear()
                else:
                    if snEnd == 9:
                        snStart = 0
                        snEnd = 3
                        rnStart += 3
                        rnEnd += 3
                        l.clear()
                        continue
                    else:
                        l.clear()
                        snStart += 3
                        snEnd += 3
                        continue
        a += 1
        
    l = []
    s = 0
    e = 1
   

    while e < len(sudoku):
        if answer == False:
            break
        else:
            for x in sudoku:
                for j in x[s:e]:
                    l.append(j)
            s += 1
            e += 1
            if len(l) == 9:
                l = [i for i in l if i != 0]
                if len(l) != len(set(l)):
                    answer = False
                    l.clear()
                else:
                    l.clear()
                    continue
    return answer


if __name__ == "__main__":
    sudoku  = [[1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    tulosta(sudoku)
    print(sudoku_oikein(sudoku))
    strike = 0
    while True:
        if sudoku_oikein(sudoku) == True:
            answer = input("Insert line, column and number (example 0,1,2):")
            if answer == "-1":
                break
            else:
                a = answer.split(",")
                a = list(map(int, a))
                lisays(sudoku, a[0], a[1], a[2])
                tulosta(sudoku)       
        elif sudoku_oikein(sudoku) == False:
            strike += 1
            if strike == 3:
                break
            else:
                print(f"Wrong {strike}")
                continue
            
    """tulosta(sudoku)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)"""
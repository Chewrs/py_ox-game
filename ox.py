import os

bd = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display():
    i = 0
    while i < 9:
        print(bd[i], end=" ")
        if i == 2 or i == 5 or i == 8:
            print()
        i += 1


def win():
    for i in range(0, 9, 3):
        if bd[i] == bd[i + 1] == bd[i + 2]:
            return False
    # Check columns
    for i in range(3):
        if bd[i] == bd[i + 3] == bd[i + 6]:
            return False

    # Check diagonals
    if bd[0] == bd[4] == bd[8] or bd[2] == bd[4] == bd[6]:
        return False


def write(player):
    while 1:
        wt = int(input(f"{player}:"))
        if isinstance(bd[wt - 1], int):
            bd[wt - 1] = f"{player}"
            break

        else:
            os.system("clear")
            display()


display()
while 1:
    write("x")
    os.system("clear")
    display()
    if win() == False:
        print("x win")
        break

    write("o")
    os.system("clear")
    display()
    if win() == False:
        print("o win")
        break

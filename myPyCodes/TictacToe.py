from typing import Final

set_index: Final = 1   # To manage the indices
TTT: list[str | int] = ['0', '0', '0', '0', '0', '0', '0', '0', '0']  # Stores the values of Tic Tac Toe


def show_ttt_matrix(elements: list):
    if len(elements) != 9:
        raise "length should be equal to 9"
    print(elements[0:3], elements[3:6], elements[6:9], sep="\n", end="\n \n")


def u1_choice(u1_symbol):  # u1 -> User1
    choice = int(input(f"Enter spot for {u1_symbol} : ")) - set_index

    if choice > 8:
        print("\nSpot is > 9.\n")
        u1_choice(u1_symbol)
        return

    if any([TTT[choice] == 'X', TTT[choice] == 'O']):
        print("\nYou entered existed spot, Please enter again.\n")
        u1_choice(u1_symbol)
        return

    TTT.pop(choice)
    TTT.insert(choice, u1_symbol)


def u2_choice(u2_symbol):  # u2 -> User2
    choice = int(input(f"Enter spot for {u2_symbol} : ")) - set_index

    if choice > 8:
        print("\nSpot is > 9.\n")
        u2_choice(u2_symbol)
        return

    if any([TTT[choice] == 'X', TTT[choice] == 'O']):
        print("\nYou entered existed spot, Please enter again.\n")
        u2_choice(u2_symbol)
        return

    TTT.pop(choice)
    TTT.insert(choice, u2_symbol)


def play(u1=u1_choice, u2=u2_choice, u1_symbol='O', u2_symbol='X'):
    for i in range(1, len(TTT)-3):
        show_ttt_matrix(TTT)
        u1(u1_symbol)
        show_ttt_matrix(TTT)
        if i == 5:
            break
        u2(u2_symbol)


def check_winner():
    # c1 -> element in column 1
    # r1 -> element in row 1
    # The loop is used to skip every rom,column and diagonal

    r1 = c1 = 0
    r2 = c2 = 1
    r3 = c3 = 2

    for i in range(0, 3):

        # For, to check rows.
        if TTT[r1+(3*i)] == TTT[r2+(3*i)] == TTT[r3+(3*i)]:
            print("WINNER is ", TTT[r2+(3*i)])
            break
        # For, to check columns.
        elif TTT[c1+i+0] == TTT[c2+i+2] == TTT[c3+i+4]:
            print("WINNER is ", TTT[r2+i])
            break
        # For, to check diagonals.
        elif i < 2:
            if TTT[0+(i*2)] == TTT[4] == TTT[8-(i*2)]:
                print("WINNER is ", TTT[4])
        break


play()
check_winner()

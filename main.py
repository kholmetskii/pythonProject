a = [[' ', ' ', ' ', ],
     [' ', ' ', ' ', ],  # make matrix 3x3 with spaces
     [' ', ' ', ' ', ]]


def if_occupied_out_of_range_type_error(x,
                                        y):  # function that check if that fiels is occupied or out of range or type error
    if (x == '1' or x == '2' or x == '3') and (y == '1' or y == '2' or y == '3') and (a[int(x) - 1][int(y) - 1] == ' '):
        return False
    else:
        return True


def swap_turn(turn):  # function that change turn
    if turn == 'X':
        return 'O'
    elif turn == 'O':
        return 'X'


def if_draw(a):  # if matrix does not have ' ' it means that there is a draw
    if ' ' in (a[0] and a[1] and a[2]):
        return False
    else:
        return True


def if_win(turn):
    if a[0][0] == a[0][1] == a[0][2] == turn or a[1][0] == a[1][1] == a[1][2] == turn or a[2][0] == a[2][1] == a[2][
        2] == turn or a[0][0] == a[1][0] == a[2][0] == turn or a[0][1] == a[1][1] == a[2][1] == turn or a[0][2] == a[1][
        2] == a[2][2] == turn:
        return True  # horizontal and vertical check
    elif a[0][0] == a[1][1] == a[2][2] == turn or a[0][2] == a[1][1] == a[2][0] == turn:  # diagonal check
        return True
    else:
        return False


def print_board():  # function that prints board
    print('  1   2   3     ')
    print('1 ', a[0][0], ' | ', a[0][1], ' | ', a[0][2], ' ', sep='')
    print(' ---+---+---')
    print('2 ', a[1][0], ' | ', a[1][1], ' | ', a[1][2], ' ', sep='')
    print(' ---+---+---')
    print('3 ', a[2][0], ' | ', a[2][1], ' | ', a[2][2], ' ', sep='')


turn = 'X'  # define whose first turn
print_board()
while True:
    print()
    print('Turn:', turn)  # print whose move
    x = input('Print row :')  # input number of row
    y = input('Print column :')  # input number of column
    if if_occupied_out_of_range_type_error(x, y):  # check input if there is an error
        print('Error, try again')
        print()
        print_board()
    else:  # if there is no error
        a[int(x) - 1][int(y) - 1] = turn  # put X or O in matrix
        print_board()
        if if_win(turn):  # check if someone won
            print(turn, 'won!')
            break
        if if_draw(a):  # check if draw
            print('Draw!')
            break
        else:
            turn = swap_turn(turn)  # if game goes on then change turn

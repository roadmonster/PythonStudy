def checkwin(player):

    if diagcheck(player):
        return True
    if rowcheck(player):
        print('comes here')
        return True
    if colcheck(player):
        print('comes here')
        return True

def diagcheck(player):
    leftright = None
    rightleft = None
    for i in range(0,size):
        if board[i][i] != player:
            leftright = False

    for row in range(0,size):

        for j in range(size-1, -1, -1):
            if board[row][j] != player:
                rightleft = False

    if rightleft or leftright:
        return True
    else:
        return False


def rowcheck(player):
    row_check_result = [True]*size
    for row in range(size):
        for col in range(size):
            if board[row][col] != player:
                row_check_result[row] = False
                break
        row_check_result[row] = True

    for item in row_check_result:
        if item:
            return True
    return False




def colcheck(player):
    for col in range(0,size):
        for row in range(0,size):
            if baord[row][col] != player:
                break
        return True

    return False

def checkFinish():
    for i in range(0, size):
        for j in range(0,size):
            if board[i][j] == 0:
                return False

    return True


size = int(input('What size of the board do you want?'))

board = [[0 for i in range(0,size)]for j in range(size)]

print(board)

for i in range(0,size):
    for j in range(0,size):
        board[i][j] = 0

p1 = input('Player1 enter your name')
p2= input('Player2 enter your name')

gameDone = False
p1flag = 1

winner = None
drawgame = False
while not gameDone:

    row = int(input('Enter your row:'))
    col = int(input('Enter your col:'))

    if board[row-1][col-1] == 0:
        if p1flag:
            board[row-1][col-1] = 1
            p1flag = 0
            print(board)

            if checkwin(1):
                winner = p1
                break

        else:
            board[row-1][col-1] = 5
            p1flag = 1
            print(board)
            if checkwin(5):
                winner = p2
                break
    else:
        print('Slot already filled, can\'t take this move')

    if checkFinish():
        gameDone = True

if drawgame:
    print('draw game')
else:
    if winner == p1:
        print('winner is {}'.format(p1))
    else:
        print('winner is {}'.format(p2))




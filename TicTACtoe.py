board = []
for i in range(3):
    (board).append(["|","|","|"])
def print_board (board):
    for row in board:
        print " ".join(row)
print_board(board)

for i in range (0,9):
    if "".join(board[0]) == "XXX" or "".join(board[1]) == "XXX" or "".join(board[2]) == "XXX":
        print "P1 wins!"
        break
    if (board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X") or (board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X") or (board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X"):
        print "P1 wins!"
        break
    if (board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X") or (board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X"):
        print "P1 wins!"
        break
    if "".join(board[0]) == "OOO" or "".join(board[1]) == "OOO" or "".join(board[2]) == "OOO":
        print "P2 wins!"
        break
    if (board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O") or (board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O") or (board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O"):
        print "P2 wins!"
        break
    if (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O") or (board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O"):
        print "P2 wins!"
        break
    if (i%2==0): # p1 turn
        a = int(input("Player 1, choose col (1-3) "))-1
        b = int(input("Player 1, choose row (1-3) "))-1
        board[b][a] = "X"
        print_board(board)
        
    else:
        a = int(input("Player 2, choose col (1-3) "))-1
        b = int(input("Player 2, choose row (1-3) "))-1
        board[b][a] = "O"
        print_board(board)


####TIC-TAC-TOE

# '''
# tic tac toe board
# [
#  {- - -}
#  {- - -}
#  {- - -}
# ]

# ##user input -->some number from 1-9
# ##if they enter anything else tell them to enter a number again!!
# ##check if user input is already taken or not
# ##add that input to the board
# ##check if user won====rows,column,diagonal
# ##toggle btw user and successful move
# '''

board=[
    ["-","-","-"],
    
    ["-","-","-"],

    ["-","-","-"]
    ]
##print(board)

def print_board(board):
    # print(board[0])
    # print(board[1])
    # print(board[2])
    for row in board:
        for slot in row:
            print(slot,end=" ")
        print()


#print_board(board)

def quit(user_input):
    if user_input=='q':
        print("THANKING FOR PLAYING :))))")
        return True
    else:
        return False

def check_input(user_input):
    ###check if the the input is btw 1 to 9
    if int(user_input)>0 and int(user_input)<10:
        return False
    else:
        return True

def istaken(cord,board):
    x=cord[0]
    y=cord[1]
    if board[x][y]!="-":
        return False
    return True
    
def cordinate(user_input):
    x=user_input//3
    y=user_input%3
    return (x,y)

def add_to_board:
    


while True:
    print_board(board)
    user_input=input("PLEASE ENTER A NUMBER FROM 1 TO 9 OR PRESS q TO QUIT?? ")
    if quit(user_input):
        break

    if check_input(user_input):
        print("PLEASE ENTER A VALID INPUT  ")
        continue
    user_input=int(user_input)
    user_input-=1

    cord=cordinate(user_input)

    if istaken(cord,board):
        print("THAT PLACE IS ALREADY TAKEN")
        print("PLEASE TRY AGAIN!!")
        continue







    

    

    



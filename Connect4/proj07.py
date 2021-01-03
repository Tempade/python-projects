#################################################################
#  CSE 231 Project 7
#
#  Functions and Mutables
#       User is given a description of Connect Four
#       User is asked to pick a color between white and black
#       User is then told what color you and your opponent is
#       User is shown the board and asked where to drop the disc
#           If an invalid column is chosen, user is asked again
#       Board is updated and game proceeds to opponents turn
#       Game continues until there is a winner!
#################################################################
pieces = {'black':'b', 'white':'w'}
COLUMN = 7
ROW = 6

def initialize(): #Function to create the empty board
    board = [[0,0,0,0,0,0,0] for n in range(ROW)]
    
    return board
    
def choose_color(): #Function to ask the user which color they want to be
    while True:
        color = input('Pick a color: ')
        if color.lower() == 'white':
            choice = ('white','black')
            print('''You are 'white' and your opponent is 'black'.''')
            break
        if color.lower() == 'black':
            choice = ('black','white')
            print('''You are 'black' and your opponent is 'white'.''')
            break
        else:
            print('''Wrong color; enter only 'black' or 'white', try again.''')
            continue
    return choice

def board_display(board): #Function to update the board after a user drops disc
    print("Current board:")
    C = COLUMN
    R = ROW
    hline = '\n' + (' ' * 2) + ('+---' * C) + '+' + '\n'
    numline = ' '.join([(' ' + str(i) + ' ') \
                        for i in range(1, C + 1)])
    str_ = (' ' * 3) + numline + hline
    for r in range(0, R):
        str_ += str(r+1) + ' |'
        for c in range(0, C):
            str_ += ' ' + \
                (str(board[r][c]) \
                     if board[r][c] is not 0 else ' ') + ' |'
        str_ += hline
    print (str_)

def drop_disc(board, column, color): #Function to drop disc at user defined spot
    column -= 1
    if column >= 7:
        return None
    if color == 'white':
        color = pieces.get('white')
    else:
        color = pieces.get('black')
    row2 = 6
    for row in reversed(board):
        if row[column] == 0:
            row[column] = color
            row2 = int(row2)
            return row2
        else:
            row2 -= 1
            continue
    if row[column] == 'w':
        print('This column is full. Please try again.')
        return 'full'
    elif row[column] == 'b':
        print('This column is full. Please try again.')
        return 'full'
    else:
        return None
    
def check_disc(board, row, column): #Function to check if there is 4 in a row
    max_vertical = -1
    min_vertical = -1
    max_horizontal = -1
    min_horizontal = -1
    row -= 1
    column -= 1
    win = False
    
    if row-1 <= -2:
        return None
    if column-1 <= -2:
        return None
            
    for i in range(4):
        
        try:
            board[row-i][column]
        except IndexError:
            pass
        else:
            max_vertical += 1
        
        try:
            board[row+i][column]
        except IndexError:
            pass
        else:
            min_vertical += 1
            
        try:
            board[row][column+i]
        except IndexError:
            pass
        else:
            max_horizontal += 1
            
        try:
            board[row][column-i]
        except IndexError:
            pass
        else:
            min_horizontal += 1

    #Set color
    for i in range(2):
        if i == 0:
            color = 'w'
        else:
            color = 'b'
            
        #Check Vertical
        if board[row][column] == color:
            
            if max_vertical >= 3:
                if board[row-3][column] == color:
                    if board[row-2][column] == color:
                        if board[row-1][column] == color:
                            win = True
            if max_vertical >= 2:
                if min_vertical >= 1:
                    if board[row-2][column] == color:
                        if board[row-1][column] == color:
                            if board[row+1][column] == color:
                                win = True
            if max_vertical >= 1:
                if min_vertical >= 2:
                    if board[row-1][column] == color:
                        if board[row+1][column] == color:
                            if board[row+2][column] == color:
                                win = True
            if min_vertical >= 3:
                if board[row+1][column] == color:
                    if board[row+2][column] == color:
                        if board[row+3][column] == color:
                            win = True
                    
        #Check Horizontal
        if board[row][column] == color:
            
            if max_horizontal >= 3:
                if board[row][column+3] == color:
                    if board[row][column+2] == color:
                        if board[row][column+1] == color:
                            win = True
            if max_horizontal >= 2:
                if min_horizontal >= 1:
                    if board[row][column+2] == color:
                        if board[row][column+1] == color:
                            if board[row][column-1] == color:
                                win = True
            if max_horizontal >= 1:
                if min_horizontal >= 2:
                    if board[row][column+1] == color:
                        if board[row][column-1] == color:
                            if board[row][column-2] == color:
                                win = True
            if min_horizontal >= 3:
                if board[row][column-1] == color:
                    if board[row][column-2] == color:
                        if board[row][column-3] == color:
                            win = True
                    
        #Check Diagonal Right
        if board[row][column] == color:
            
            if max_horizontal >= 3:
                if max_vertical >= 3:
                    if board[row-3][column+3] == color:
                        if board[row-2][column+2] == color:
                            if board[row-1][column+1] == color:
                                win = True
            if max_horizontal >= 2:
                if min_horizontal >= 1:
                    if max_vertical >= 2:
                        if min_vertical >= 1:
                            if board[row-2][column+2] == color:
                                if board[row-1][column+1] == color:
                                    if board[row+1][column-1] == color:
                                        win = True
            if max_horizontal >= 1:
                if min_horizontal >= 2:
                    if max_vertical >= 1:
                        if min_vertical >= 2:
                            if board[row-1][column+1] == color:
                                if board[row+1][column-1] == color:
                                    if board[row+2][column-2] == color:
                                        win = True
            if min_horizontal >= 3:
                if min_vertical >= 3:
                    if board[row+1][column-1] == color:
                        if board[row+2][column-2] == color:
                            if board[row+3][column-3] == color:
                                win = True
                  
        #Check Diagonal Left
        if board[row][column] == color:
            
            if max_vertical >= 3:
                if min_horizontal >= 3:
                    if board[row-3][column-3] == color:
                        if board[row-2][column-2] == color:
                            if board[row-1][column-1] == color:
                                win = True
            if max_vertical >= 2:
                if max_horizontal >= 1:
                    if min_vertical >= 1:
                        if min_horizontal >= 2:
                            if board[row-2][column-2] == color:
                                if board[row-1][column-1] == color:
                                    if board[row+1][column+1] == color:
                                        win = True
            if max_vertical >= 1:
                if max_horizontal >= 2:
                    if min_vertical >= 2:
                        if min_horizontal >= 1:
                            if board[row-1][column-1] == color:
                                if board[row+1][column+1] == color:
                                    if board[row+2][column+2] == color:
                                        win = True
            if min_vertical >= 3:
                if max_horizontal >= 3:
                    if board[row+1][column+1] == color:
                        if board[row+2][column+2] == color:
                            if board[row+3][column+3] == color:
                                win = True
                    
        
    if win == True:
        return True
    if win == False:
        return False
    
def is_game_over(board): #Function to check if the game should end or not
    draw = 0
    for i in range(6):
        test = board[i]
        if 0 not in test:
            draw += 1
    if draw == 6:
        return 'draw'
    for row in range(1,7):
        for column in range(1,8):
            if check_disc(board,row,column) == True:
                row -= 1
                column -= 1
                if board[row][column] == 'w':
                    return 'white'
                else:
                    return 'black'
            else:
                continue
    return None
    

def main(): #Function which puts all others together in one place
    banner = """
       ____ ___  _   _ _   _ _____ ____ _____ _  _   
      / ___/ _ \| \ | | \ | | ____/ ___|_   _| || |  
     | |  | | | |  \| |  \| |  _|| |     | | | || |_ 
     | |__| |_| | |\  | |\  | |__| |___  | | |__   _|
      \____\___/|_| \_|_| \_|_____\____| |_|    |_|  
    """
    intro = """
    Connect Four is a two-player connection game in which the players first choose a color and \
    then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. \
    The pieces fall straight down, occupying the lowest available space within the column. \
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 
    """
    usage = """
        Usage:
            pass:   give up, admit defeat
            exit:   exit the game
            i:      drop a disk into column i
    """
    print(banner)
    print(intro)
    print(usage)
    
    continue_game = 'yes'  # can't use "continue" because it has a special meaning
    while continue_game == 'yes':
        board = initialize()
        color = choose_color()
        board_display(board)
        turn = 'p1'
        game = True
        game_exit = False
        valid = [1,2,3,4,5,6,7]
        while game == True:
            
            while turn == 'p1':
                move = input('''{}'s turn :> '''.format(color[0]))
                if move == 'pass':
                    print('{} gave up! {} is the winner!! yay!!!'.format(color[0],color[1]))
                    game = False
                    break
                if move == 'exit':
                    game = False
                    game_exit = True
                    break
                try:
                    move = int(move)
                except ValueError:
                    print('Invalid option')
                    print(usage)
                else:
                    move = int(move)
                    if move in valid:
                        disc = drop_disc(board, move, color[0])
                        if disc == 'full':
                            continue
                        else:
                            board_display(board)
                            over = is_game_over(board)
                            if over == 'white':
                                print('white wins!')
                                game = False
                                break
                            if over == 'black':
                                print('black wins!')
                                game = False
                                break
                            if over == 'draw':
                                print('The board is full so this game ends in a draw.')
                                game = False
                                break
                            turn = 'p2'
                            break
                    else:
                        print('Invalid column: 1 <= column <= 7. Please try again.')
                        continue
                
            while turn == 'p2':
                move = input('''{}'s turn :> '''.format(color[1]))
                if move == 'pass':
                    print('{} gave up! {} is the winner!! yay!!!'.format(color[1],color[0]))
                    game = False
                    break
                if move == 'exit':
                    game = False
                    game_exit = True
                    break
                try:
                    move = int(move)
                except ValueError:
                    print('Invalid option')
                    print(usage)
                else:
                    move = int(move)
                    if move in valid:
                        disc = drop_disc(board, move, color[1])
                        if disc == 'full':
                            continue
                        else:
                            board_display(board)
                            over = is_game_over(board)
                            if over == 'white':
                                print('white wins!')
                                game = False
                                break
                            if over == 'black':
                                print('black wins!')
                                game = False
                                break
                            turn = 'p1'
                            break
                    else:
                        print('Invalid column: 1 <= column <= 7. Please try again.')
                        continue
                
        if game_exit == True:
            print("\nThanks for playing! See you again soon!")
            break

        continue_game = input("Would you like to play again? ").lower() 
    else:
        print("\nThanks for playing! See you again soon!")
    
if __name__ == "__main__":
    main()
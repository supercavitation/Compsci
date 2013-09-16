#Joshua Bloch
#4/11/13
#connect four
columns=[[1,2,3,4,5,6,7,8,9,10],['_','_','_','_','_','_','_','_','_','_']]
board=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
counter=1
def neighbor1(i, column, board):
    if column+2<=9 and board [9-i][column]=='*' and board [9-i][column+1] and board [9-i][column+2]=='*':
            return 'Victory!'
        
    if board [9-i-1][column-1]=='*':
        if board [9-i-2][column-1]=='*':
            if board [9-i-3][column-1]=='*':
                return 'Victory!'
            if 9-i+1<=9 and board [9-i+1][column-1]=='*':
                return 'Victory!'
        if 9-i+2<=9 and board [9-i+1][column-1]=='*' and board [9-i+2][column-1]=='*':
            return 'Victory!'
    if 9-i+3<=9 and board [9-i+1][column-1]=='*' and board [9-i+2][column-1]=='*' and board [9-i+3][column-1]=='*':
        return 'Victory!'
    

while True:
    for i in range(0,2):
        for j in range(0,10):
            print columns[i][j],
        print
    for i in range(0,10):
        for j in range(0,10):
            print board [i][j],
        print

    if counter==1:
        column=int(raw_input('Player 1, choose a column:'))
        for i in range (0,10):
            if board [9-i][column-1]==0:
                board [9-i][column-1]='*'
                break
        counter=2
        victoryChecker=neighbor1(i, column, board)
    elif counter==2:
        column=int(raw_input('Player 2, choose a column:'))
        for i in range (0,10):
            if board [9-i][column-1]==0:
                board [9-i][column-1]='#'
                break
        counter=1

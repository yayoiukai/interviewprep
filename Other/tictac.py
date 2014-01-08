## Very simple tictac toe game 
gamemap = [[0 for x in xrange(3)] for x in range(3)] 
boardmap = [[0 for x in range(5)] for x in range(3)]

def setup_board():
    for i in range(0,3):
        for j in range(0,3):
        	gamemap[i][j] = 0

    for i in range(0,3):
    	for j in range(0,5):
    		if j % 2 != 0:
    		    boardmap[i][j] = "|"
    		    
    		else:
    			boardmap[i][j] = " "
    			


def print_board():
    line = ''
    for i in range(0,3):
    	for j in range(0,5):
    			line = line + boardmap[i][j]
    	line = line + "\n"
    print line 

def check_winner():
    message =0
    player1 = []
    player1v = []
    player2 = []
    player2v = [] 
   
    #check horizontal and vertical 
    for i in range(3):
    	for j in range(3):
    		if gamemap[i][j] == 1:
    		    player1.append(1)
    		   
    		elif gamemap[i][j] == 2:
    			player2.append(2)
    			
    		elif gamemap[j][i] == 1:
    			player1v.append(1)
    		
    		elif gamemap[j][i] == 2:
    			player2v.append(2)
    		
    	if len(player1) == 3 or len(player1v) == 3:
    		message = 1
    	elif len(player2) == 3 or len(player2v) == 3:
    		message = 2
    	else:
    	    player1 = []
    	    player2 = []
    	    player1v = []
    	    player2v = []

    player1 = []
    player2 = []
    player1v = []
    player2v = []

    #check diagnol
    for i in range(0,3):
    	if gamemap[i][i] == 1:
    	    player1.append(1)
           
    	elif gamemap[i][i] == 2:
    	    player2.append(2)
    	 
    	if gamemap[i][2-i] == 1:
    		player1v.append(1)
    		
    	elif gamemap[i][2-i] == 2:
    		player2v.append(2)

    if len(player1) == 3 or len(player1v) == 3:
    	message = 1
    	return message
    elif len(player2) == 3  or len(player2v) == 3:
    	message = 2
    	return message
    else:
        player1 = []
    	player2 = []
    	player1v = []
    	player2v = []
    
    return message 

def take_turn(n):
    prompt = "turn: " + str(n) + "\n"
    x = raw_input(prompt)
    a = x.split(',')
    x = int(a[0])
    y = int(a[1])
    if gamemap[y][x] == 0:
    	gamemap[y][x] = n
    	if x == 1:
	        x = 2
        elif x == 2:
	        x = 4

        if n == 1:
            boardmap[y][x] = 'O'
        else:
            boardmap[y][x] = 'X'
    else:
    	print "The spot is taken. Please make another input"
    	take_turn(n)

   




def play_game():
    print "Let's play tic tac toe"
    print "please input x,y cordinate of the location e.g 1,1"
    print "the range of the coordinate is 0 to 2 for both x and y"
    setup_board()
    print_board()
    message = 0
    n = 1
    count = 0 
    while message == 0:
        if n == 1:
            take_turn(1)
            n = 2 
        else:
            take_turn(2)
            n = 1
        print_board()
        message = check_winner()
        count += 1 
        if count == 9:
        	break
    
    if message > 0:
        print "Player ", message, " won"
    else:
    	print "Tie!!!"


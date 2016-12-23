class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for i in range(0,W):
            s+= ' ' + str(i%10)# and the numbers underneath here
        
        return s       # the board is complete, return it
    def addMove(self,col,ox):
        H= self.height
        W= self.width
        for row in range(H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox
    def clear(self):
        H= self.height
        W= self.width
        for row in range(H):
            for col in range(W):
                self.data[row][col] = ' '
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    def allowsMove(self, c):
        if c not in range(self.width):
            return False
        elif c>=self.width:
            return False
        elif self.data[0][c] != ' ':
            return False
        else:
            return True
    def isFull(self):
        for c in range(self.width):
            x=0
            if self.allowsMove(c) == False:
                x+=1
        if x ==self.width-1:
            return True
        else:
            return False

    def delMove(self,c):
        for row in range(self.height):
            if self.data[row][c] == 'X' or self.data[row][c] =='O':
                self.data[row][c] = ' '
                return
    def winsFor(self,ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True
        #check for vertical wins
        for row in range(0,H-3):
            for col in range(0,W):
                if D[row][col] == ox and\
                   D[row+1][col] == ox and\
                   D[row+2][col] == ox and\
                   D[row+3][col] == ox:
                    return True
        #check for diagonal wins(South East)
        for row in range(3,H):
            for col in range(0,W-3):
                if D[row][col] == ox and\
                   D[row-1][col+1] == ox and\
                   D[row-2][col+2] == ox and\
                   D[row-3][col+3] == ox:
                    return True
        #check for diagonal wins(NE)
        for row in range(0,H-3):
            for col in range(0,W-3):
                if D[row][col] == ox and\
                   D[row+1][col+1] == ox and\
                   D[row+2][col+2] == ox and\
                   D[row+3][col+3] == ox:
                    return True
        return False
    def hg(self):
        print 'Welcome!'
        while True:
            print self
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("X's Choice: ")
            self.addMove(users_col,'X')
            if self.winsFor('X'):
                break
            print self
            users_coR = -1
            while self.allowsMove( users_coR ) == False:
                users_coR = input("O's Choice: ")
            self.addMove(users_coR,'O')
            if self.winsFor('O'):
                break
        if self.winsFor('X')==True:
            print 'X wins! Congrats'
        elif self.winsFor('O')==True:
            print 'O wins! Congrats'
        print self
            

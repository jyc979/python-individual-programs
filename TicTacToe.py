def print2d( A ):
    """ print2d prints a 2d array, A
        as rows and columns
        input: A, a 2d list of lists
        output: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR): # NR = =numrows
        for c in range(NC):  # NC == numcols
            print A[r][c],
        print

    return None  # this is implied anyway,
    # when no return statement is present

# some tests for print2d
A = [ ['X',' ','O'], ['O','X','O'] ]
print "2-row, 3-col A is"
print2d(A)

A = [ ['X','O'], [' ','X'], ['O','O'], ['O','X'] ]
print "4-row, 2-col A is"
print2d(A)


# create a 2d array from a 1d string
def createA( NR, NC, s ):
    """ returns a 2d array with
        NR rows (numrows) and
        NC cols (numcols)
        using the data from s: across the
        first row, then the second, etc.
        We'll only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [ s[0] ] # add that char
            s = s[1:]   # get rid of that first char
        A += [newrow]
    return A

# a couple of tests for createA:
A = [ ['X',' ','O'], ['O','X','O'] ]
newA = createA( 2, 3, 'X OOXO')
print "Is newA == A? Should be True:", newA == A

A = [ ['X','O'], [' ','X'], ['O','O'], ['O','X'] ]
newA = createA( 4, 2, 'XO XOOOX')
print "Is newA == A? Should be True:", newA == A

def row3east(ch,rowS,colS,A):
    Arow = len(A)
    Acol = len(A[0])
    if rowS <= Arow-1 == False:
        return False
            #elif rowS+2>2:
                #return False
    elif colS<= Acol-1 == False:
        return False
    elif colS+2>3:
        return False
    elif A[rowS][colS] == A[rowS][colS+1]==A[rowS][colS+2]:
        return A[rowS][colS] == ch
    else:
        return False

def row3south(ch,rowS,colS,A):
    Arow = len(A)
    Acol = len(A[0])
    if rowS<=Arow-1 == False:
        return False
    elif colS<=Acol-1 == False:
        return False
    elif rowS+2>3:
        return False
    elif A[rowS][colS]==A[rowS+1][colS]==A[rowS+2][colS]:
        return A[rowS][colS] == ch
    else:
        return False
def row3se(ch,rowS,colS,A):
    Arow = len(A)
    Acol = len(A[0])
    if rowS<=Arow-1 == False:
        return False
    elif rowS+2>3 or colS+2>3:
        return False
    elif colS<=Acol-1 == False:
        return False
    elif A[rowS][colS]==A[rowS+1][colS+1]==A[rowS+2][colS+2]:
        return A[rowS][colS] == ch
    else:
        return False
def row3ne(ch,rowS,colS,A):
    Arow = len(A)
    Acol = len(A[0])
    if rowS<=Arow-1 == False:
        return False
    elif colS>= Acol or colS+1>Acol or colS+2>Acol:
        return False
    elif rowS >= Arow or rowS-1<0 or rowS-2<0:
        return False
    elif colS<=Acol-1 == False:
        return False
    elif A[rowS][colS] == A[rowS-1][colS+1] == A[rowS-2][colS+2]:
        return A[rowS][colS] == ch
    else:
        return False
def inarow_Neast(ch,rstart,cstart,A,N):
    Arow = len(A)
    Acol = len(A[0])
    if rstart>=Arow:
        return False
    elif cstart>=Acol:
        return False
    elif cstart + N > Acol:
        return False
    x = 0
    for i in range(N):
        x = x+i
        if A[rstart][cstart+x] == A[rstart][cstart]:
            x= x+1
        elif A[rstart][cstart+x] == A[rstart][cstart]:
            x=x+0
        if x==N:
            return A[rstart][cstart] == ch
        else:
            return False
def inarow_Nsouth(ch,rstart,cstart,A,N):
    Arow = len(A)
    Acol = len(A[0])
    if rstart>=Arow:
        return False
    elif cstart>=Acol:
        return False
    elif rstart+N>Arow:
        return False
    x = 0
    for i in range(N):
        if A[rstart+x][cstart] == A[rstart][cstart]:
            x =x+1
        elif A[rstart+x][cstart] == A[rstart][cstart]:
            x=x+0
        if x== N:
            return A[rstart][cstart] == ch
    else:
        return False

def inarow_Nse(ch,rstart,cstart,A,N):
    Arow=len(A)
    Acol=len(A[0])
    if rstart>=Arow:
        return False
    elif cstart>=Acol:
        return False
    elif rstart+N>Arow:
        return False
    elif cstart+N>Acol:
        return False
    x=0
    for i in range(N):
        if A[rstart+x][cstart+x]==A[rstart][cstart]:
            x = x+1
        elif A[rstart+x][cstart+x] == A[rstart][cstart]:
            x = x+0
        if x ==N:
            return A[rstart][cstart] == ch
    else:
        return False
        
def inarow_Nne(ch,rstart,cstart,A,N):
    Arow = len(A)
    Acol = len(A[0])
    if rstart>=Arow:
        return False
    elif cstart >=Acol:
        return False
    elif cstart+N>Acol:
        return False
    elif rstart+1-N<0:
        return False
    x=0
    for i in range(N):
        if A[rstart-x][cstart+x] == A[rstart][cstart]:
            x=x+1
        elif A[rstart-x][cstart+x] == A[rstart][cstart]:
            x= x+0
        if x==N:
            return A[rstart][cstart]==ch
    else:
        return False
        
            

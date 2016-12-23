# python 2
#
# Homework 9, Problem 1
# Game of Life
#
# Name:
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]   # What do you need to add a whole row here?
    return A
def pB(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w,h):
    A = createBoard(w,h)
    for i in range(1,h-1):
        for j in range(1,w-1):
            A[i][j] = 1
    return A
def randomCells(w,h):
    a = createBoard(w,h)
    for i in range(1,h-1):
        for j in range(1,w-1):
            a[i][j] = random.choice([0,1])
    return a
def copy(a):
    h = len(a)
    w = len(a[0])
    A = createBoard(w,h)
    for i in range(h):
        for j in range(w):
            A[i][j] = a[i][j]
    return A
def innerReverse(a):
    h = len(a)
    w = len(a[0])
    A = createBoard(w,h)
    for i in range(1,h-1):
        for j in range(1,w-1):
            if a[i][j] ==0:
                A[i][j] = 1
            elif a[i][j] == 1:
                A[i][j] = 0
    return A       
def countNeighbors(row,col,a):
    x=0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if a[i][j] == 1:
                x +=1
    if a[row][col]==1:
        return x-1
    return x
def nlg(A):
    newA = copy(A)
    h= len(A)
    w= len(A[0])    
    for i in range(1,h-1):
        for j in range(1,w-1):
            if A[i][j] == 0 and countNeighbors(i,j,A)==3:
                newA[i][j] = 1
            if countNeighbors(i,j,A)<2:
                newA[i][j] = 0
            if countNeighbors(i,j,A)>3:
                newA[i][j] = 0
    return newA
            
    
            
            

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.


def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def mutate0(i,oldL):
    x = 2*oldL[i]
    return x

def mutate1(i,oldL):
    x = oldL[i]**2
    return x

def mutate2(i,oldL):
    return oldL[i-1]

def mutate3(i,oldL):
    x = choice([0,1])
    return x
def allones(L):
    if L==[]:
        return True
    elif L[0]==1:
        return allones(L[1:])
    else:
        return False
    
def mutate4(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        new_ith_element = 1        # this makes the game easy!
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element

def mutate5(i, oldL, user=0):
    if i == user:
        new_ith_element = 1-oldL[i]      
    else:
        new_ith_element = oldL[i]
    return new_ith_element

def mutate6(i, oldL, user=0):
    if i == user or i==user-1 or i ==user+1:
        new_ith_element = 1-oldL[i]      

    else:
        new_ith_element = oldL[i]
    return new_ith_element

def randBL(N):
    return [choice([0,1]) for i in range(N)]

def evolve(oldL, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print range(len(oldL))
    print oldL,                    # print the old list, L
    print '(G:' + str(curgen)+')'
    time.sleep(0.25)
    
    if allones(oldL)==True:  # we're done!
        return curgen
    else:
        user = choice(range(len(oldL)))
        newL = [ mutate6(i, oldL,user) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)

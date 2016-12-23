def isodd(n):
    if n%2==1:
        return True
    elif n%2==0:
        return False
def numToBinary(N):
  if N == 0:
    return ''
  elif N%2 == 1:
    return numToBinary((N-1)/2)+ '1'
  else:
    return  numToBinary(N/2) + '0'
def binaryToNum(S):
  if S == '':
    return 0
  elif S[-1] == '1': 
    return  int(binaryToNum(S[:-1]))*2 + 1
  else: 
    return  int(binaryToNum(S[:-1]))*2 + 0
def increment(s):
    x = binaryToNum(s)+1
    y = numToBinary(x)
    if s == '1'*8:
        return '0'*8
    elif len(y) <=8:
        return '0'*(8-len(y))+y
def count(s,n):
    if n == 0:
        print s
    else:
        print s
        return count(increment(s),n-1)
    
def numToTernary(N):
    if N ==0:
        return ''
    elif N%3 == 1:
        return numToTernary((N-1)/3)+'1'
    elif N%3 == 2:
        return numToTernary((N-2)/3)+'2'
    else:
        return numToTernary(N/3)+'0'
def ternaryToNum(s):
    if s == '':
        return 0
    elif s[-1] == '1':
        return int(ternaryToNum(s[:-1]))*3 + 1
    elif s[-1] == '2':
        return int(ternaryToNum(s[:-1]))*3 + 2
    else:
        return int(ternaryToNum(s[:-1]))*3 + 0
def balancedTernaryToNum(s):
    if s == '':
        return 0
    elif s[-1] == '-':
        return int(balancedTernaryToNum(s[:-1]))*3 -1
    elif s[-1] == '0':
        return int(balancedTernaryToNum(s[:-1]))*3
    else:
        return int(balancedTernaryToNum(s[:-1]))*3 + 1

def balancedNumToTernary(s):
    if s ==0:
        return ''
    elif s%3 == 1:
        return balancedNumToTernary((s-1)/3)+'+'
    elif s%3 == 2:
        return balancedNumToTernary((s+1)/3)+'-'
    else:
        return balancedNumToTernary(s/3) + '0'
 
def numToBaseB(x,y):
    if x == 0:
        return ''
    elif x%y != 0:
        return numToBaseB((x-(x%y))/y,y) + str(x%y)
    else:
        return numToBaseB((x-(x%y))/y,y) + '0'

def baseBToNum(x,y):
    if x == '':
        return 0
    elif x[-1] != '0':
        return int(baseBToNum(x[:-1],y))*y + int(x)%y
    else:
        return int(baseBToNum(x[:-1],y))*y

def baseTobase(x,y,z):
    a = baseBToNum(z,x)
    return numToBaseB(a,y)
def add(x,y):
    a = binaryToNum(x)
    b = binaryToNum(y)
    return numToBinary(a+b)

def carry(x,y):
    if x =='' or y =='':
        return ''
    elif int(x[-1])+int(y[-1]) ==2:
        return carry(x[:-1],y[:-1]) + '1'
    else:
        return carry(x[:-1],y[:-1]) + '0'

def addB(x,y):
    if x =='' or y =='':
        return ''
    elif int(x[-1])+int(y[-1])+int(carry(x[-1],y[-1]))==3:
        return addB(addB(x[:-1],y[:-1]),carry(x[-1:],y[-1:]))+'1'
    elif int(x[-1])+int(y[-1])+int(carry(x[-1],y[-1]))==2:
        return addB(addB(x[:-1],y[:-1]),carry(x[-1:],y[-1:]))+'0'
    elif int(x[-1])+int(y[-1])+int(carry(x[-1],y[-1]))==1:
        return addB(x[:-1],y[:-1])+'1'
    elif int(x[-1])+int(y[-1])+int(carry(x[-1],y[-1]))==0:
        return addB(x[:-1],y[:-1])+'0'

def check(s):
    if s == '':
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return check(s[1:])
def countC(s):
    
    if s =='':
        return len(s)
    else:
        x = countC(s[1:])+1
        if check(s)==False:
            return x 
        else:
            return x-1
def compress(s):
    if s =='':
        return 0
    elif s[0] != s[-1]:
        return s[0]+'0'*6+'1'
    else:
        x = compress(s[1:])+1
        if s[0] == s[1]:
            return x
        elif s[0] != s[1]:
            return s[0]+ (8*'0'-x*'0')+numToBinary(x)
    
    

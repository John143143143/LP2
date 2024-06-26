#size of board
# N = int(input())
N = 6

#board
b=[[0]*N for i in range(N)]

# b=[]

# for j in range(N):
#     temp=[]
#     for i in range(N):
#         temp.append(0)
#     b.append(temp)

# print(b)

def isSafe(i,j):
    
    # Horizontal&Vertical check for queen Attack
    for p in range(N):
        if b[i][p]==1 or b[p][j]==1:
            return False
        
    #Diagonal check for Queen Attack
    for n in range(N):
        for m in range(N):
            if i+j == n+m or i-j == n-m:
                if b[n][m] == 1:
                    return False
                
    return True



def nqueen(noq):

    if noq == 0:
        return True
    
    for i in range(N):
        for j in range(N):
            if b[i][j] != 1 and isSafe(i,j):
                b[i][j]=1
                if nqueen(noq-1) == True:
                    return True
                b[i][j]=0
    return False

def printBoard(b):
    for i in b:
        print(i)

if nqueen(N):
    printBoard(b)
else:
    print("can't place")
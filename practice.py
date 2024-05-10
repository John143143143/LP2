# g = {
#     0:[1,2],
#     1:[0,3,4],
#     2:[3,0],
#     3:[0,1,4],
#     4:[1,3]
# }

# def dfs(g,s):
#     vis[s]=1
#     print(s)
#     for c in g[s]:
#         if not vis[c]:
#             dfs(g,c)

# vis = [0]*5

# dfs(g,0)

# def bfs(g,s):
#     q=[s]
#     vis=[s]
#     while q:
#         cur = q.pop(0)
#         print(cur)
#         for c in g[cur]:
#             if c not in vis:
#                 q.append(c)
#                 vis.append(c)
# bfs(g,0)


# def selection_sort(a):

#     for i in range(len(a)-1):
#         min_index = i
#         for j in range(i,len(a)):
#             if a[min_index] > a[j]:
#                 min_index=j
#         a[min_index],a[i] = a[i],a[min_index]

# a=[7,3,9,4,1,5]
# print("Unsorted Array",a)
# selection_sort(a)
# print("Sorted Array",a)

# N=int(input("Size : "))

# b= [[0]*N for i in range(N)]

# def isSafe(i,j):

#     for p in range(N):
#         if b[i][p] == 1 or b[p][j] == 1:
#             return False
    
#     for m in range(N):
#         for n in range(N):
#             if i+j == m+n or i-j == m-n :
#                 if b[m][n]==1:
#                     return False
    
#     return True

# def nqueen(noq):

#     if noq == 0:
#         return True
    
#     for i in range(N):
#         for j in range(N):
#             if b[i][j]!=1 and isSafe(i,j):
#                 b[i][j]=1
#                 if nqueen(noq-1) == True:
#                     return True
#                 b[i][j]=0
    
#     return False

# def printBoard(b):
#     for i in b:
#         print(i)

# if nqueen(N):
#     printBoard(b)
# else:
#     print("Can't place")

# import time
# now = time.time()

# qna={
#     "hi":"hey",
#     "how are you?":"I am fine",
#     "what is your name":"my name is sainath",
#     "how old are you?" : "I am 20 years old",
#     "what is time now":now
# }

# while True:
#     qs = input()
#     if qs == "quit":
#         break
#     else:
#         print(qna[qs])

# problem_dic = {
#     "printer not working":"check that it's turned on and connect to the network",
#     "can't log in":"make sure using the corrected username and password.",
#     "software not installing":"check that your compute meets system requirements.",
#     "internet not working":"restart the modem or router",
#     "email not sending":"check that youre using the corrected email server setting"
# }

# def handle_request(user_input):

#     if user_input == "exit":
#         return "GoodBye!"     
#     elif user_input in problem_dic:
#         return problem_dic[user_input]
#     else:
#         return "I'm sorry, I don't know how to help with that problem."

# while True:
#     user_input = input("What's the problem? type 'exit' to quit")
#     response = handle_request(user_input)
#     print(response)
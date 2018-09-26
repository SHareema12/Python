import random

def smallparsimony(T, root):

    if(W[L[root]] == ''):
        smallparsimony(T, L[root])

    if(W[R[root]] == ''):
        smallparsimony(T, R[root])

    if(W[L[root]] != '' and W[R[root]] != ''):
        l = L[root]
        r = R[root]
        if(len(set(W[l]).intersection(set(W[r]))) != 0):
            W[root] = set(W[l]).intersection(set(W[r]))
        else:
            W[root] = set(W[l]).union(set(W[r]))             

def assignsequences(T, root):
    
    if(L[root] == -1 and R[root] == -1):
        return

    p = P[root]
    if(p == -1):
        n = random.choice(list(W[root]))
        S[root] += n
        W[p] = n
    elif(W[p] in W[root]):
        S[root] += W[p]
    else:
        S[root] += random.choice(list(W[root]))
        
    assignsequences(T, L[root])
    assignsequences(T, R[root])


def getparsimonyscore(T, root, score):
    print("Current root", root)
    print ("Score from previous call", score)
    if (L[root] == -1 and R[root] == -1):
        return score
    else:
        for i in range(0, len(S[root]), 1):
            if (S[root][i] != S[L[root]][i]):
                score = score + 1

            if (S[root][i] != S[R[root]][i]):
                score = score + 1
        print("New score", score)
       
    score = getparsimonyscore(T, L[root],score)
    score = getparsimonyscore(T, R[root],score)
    ##if left and right child are -1 then do nothing and return score
    ##else
    ##get Hamming distance between root and left child, and between
    ##root and right child, and add it to score
    ##Then call getparsimony(T, L[root], score)
    ##and call getparsimony(T, R[root], score)

    return score

###############
### Main
###############

P = [4, 4, 5, 5, 6, 6, -1]
L = [-1, -1, -1, -1, 0, 2, 4]
R = [-1, -1, -1, -1, 1, 3, 5]
S = ['AAC', 'CAG', 'CGC', 'GGC', '', '', '']

nleaves = 4
totalnodes = (2*nleaves) - 1
rootNode = totalnodes-1 
for i in range(0, len(S[0]), 1):
    W = []
    for j in range (0, nleaves, 1):
        W.append(S[j][i])
    for j in range(nleaves, totalnodes, 1):
        W.append('')
    T = [P, L, R, S, W]
    smallparsimony(T, rootNode)
    assignsequences(T, rootNode)

print("Tree:")
print(T[0])
print(T[1])
print(T[2])
print(T[3])

print (S[6][1]) 

print ("Final Parsimony Score:" , getparsimonyscore(T,totalnodes -1,0))



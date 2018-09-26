import random

def smallparsimony(T, root):
        L = T[1]
        R = T[2]
        W = T[4]

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

	P = T[0]
	L = T[1]
	R = T[2]
	S = T[3]
	W = T[4]
	
	if(L[root] == -1 and R[root] == -1):
		return

	p = P[root]
	if(p == -1):
		n = random.choice(list(W[root]))
		S[root] += n
		W[root] = n
	elif(W[p] in W[root]):
		S[root] += W[p]
		W[root] = W[p]
	else:
		r = random.choice(list(W[root]))
		S[root] += r
		W[root] = r
		
	assignsequences(T, L[root])
	assignsequences(T, R[root])

def getparsimonyscore(T, root, score):

	##if left and right child are -1 then return score
	##else
	##get Hamming distance between root and left child, and between
	##root and right child, and add it to score
	##Then call getparsimony(T, L[root], score)
	##and call getparsimony(T, R[root], score)

	L = T[1]
	R = T[2]
	S = T[3]

	##For Hamming distance
	if(L[root] == -1 and R[root] == -1):
		return score

	h = 0
	for i in range(0, len(S[root]), 1):
		if(S[root][i] != S[L[root]][i]):
			h += 1
	score += h

	h = 0
	for i in range(0, len(S[root]), 1):
		if(S[root][i] != S[R[root]][i]):
			h += 1
	score += h

	score = getparsimonyscore(T, L[root], score)
	score = getparsimonyscore(T, R[root], score)
	
	return score

def parsimonyscore(T):

	P = T[0]
	L = T[1]
	R = T[2]
	S = T[3]
	
	nleaves = (len(P) + 1)/2
	nnodes = (2 * nleaves) - 1
	for i in range(0, len(S[0]), 1):
        	W = []
        	for j in range(0, nleaves, 1):
                        W.append(S[j][i])
                for j in range(nleaves, nnodes, 1):
                        W.append('')
                T = [P, L, R, S, W]
		smallparsimony(T, nnodes-1)
		assignsequences(T, nnodes-1)

	score = getparsimonyscore(T, nnodes-1, 0)
	return score

###############
### Main
###############

#P = [4, 4, 5, 5, 6, 6, -1]
#L = [-1, -1, -1, -1, 0, 2, 4]
#R = [-1, -1, -1, -1, 1, 3, 5]
#S = ['AAC', 'CAG', 'CGC', 'GGC', '', '', '']

#    0  1  2  3  4  5  6   7  8  9   10
P = [6, 6, 8, 7, 7, 9, 10, 8, 9, 10, -1 ]
L = [-1,-1,-1,-1,-1,-1, 0, 3, 2, 5,   6]
R = [-1,-1,-1,-1,-1,-1, 1, 4, 7, 8,   9]
S = ['AC', 'CC', 'AG', 'GG', 'CT', 'CG', '', '', '', '', '']

T = [P, L, R, S]

print("Tree:")
print(T[0])
print(T[1])
print(T[2])
print(T[3])

pscore = parsimonyscore(T)

print("Tree:")
print(T[0])
print(T[1])
print(T[2])
print(T[3])

print(pscore)

import random
import smallparsimony

#Start with a random tree T

def newick(root, newick_tree, L, R):
    l = L[root]
    r = R[root]
    if l == -1 and r == -1:
        name = data[2*root]
        newick_tree = newick_tree + name
        return newick_tree
    else:
        newick_tree = newick_tree + "("
        newick_tree = newick(l, newick_tree, L, R)
        newick_tree = newick_tree + ","
        newick_tree = newick(r, newick_tree, L, R)
        newick_tree = newick_tree + ")"
        return newick_tree

def randomtree(T, nnodes, nleaves):

	P = T[0]
	L = T[1]
	R = T[2]
	S = T[3]

	for i in range(0, nnodes, 1):
		P.append(0)
		if(i < nleaves):
			L.append(-1)
			R.append(-1)
			S.append(data[i*2+1])
		else:
			L.append(0)
			R.append(0)
			S.append('')
	pool = []
	for i in range(0, nleaves, 1):
		pool.append(i)

	done = 0
	i = 0
	while(not done):
		r1 = random.choice(pool)
		pool.remove(r1)
		r2 = random.choice(pool)
		pool.remove(r2)
		pool.append(nleaves + i)
		P[r1] = nleaves + i
		P[r2] = nleaves + i
		L[nleaves+i] = r1
		R[nleaves+i] = r2
		i = i + 1
		if(len(pool) == 1):
			done = 1


	P[nnodes-1] = -1
	return

def NNI(T, root, flag, trueroot):
	P = T[0]
	L = T[1]
	R = T[2]
	S = T[3]

	#perform the NNI move
	if(root != trueroot):	
		u = root
		v = L[u]
		if(L[v] == -1 and R[v] == -1):
			return
		#Use flag to determine the NNI move
		if(flag == 0):
			temp = L[v]
			L[v] = R[u]
			R[u] = temp
			P[L[v]] = v
			P[R[u]] = u
		elif(flag == 1):
			temp = R[v]
			R[v] = R[u]
			R[u] = temp
			P[R[v]] = v
			P[R[u]] = u
		return		
	else:
		u = root
		v = L[u]
		w = R[u]
		if(L[v] == -1 and R[v] == -1):
			return
		if(L[w] == -1 and R[w] == -1):
			return
		#Use flag to determine the NNI move
		if(flag == 0):
			temp = L[v]
			L[v] = L[w]
			L[w] = temp
			P[L[v]] = v
			P[L[w]] = w
		elif(flag == 1):
			temp = R[v]
			R[v] = L[w]
			L[w] = temp
			P[R[v]] = v
			P[L[w]] = w
		return		

################
##### Main #####
################

f = open("dna.fasta")
#f = open("haemoglobin.aligned.fasta")
data = f.readlines()

for i in range(0, len(data), 1):
	data[i] = data[i].strip('\n')

nleaves = int(len(data)/2)
nnodes = (2*nleaves) - 1

P = []
L = []
R = []
S = []
T = [P, L, R, S]
randomtree(T, nnodes, nleaves)

#while(p does not change):

print(P)
print(L)
print(R)
print(S)

##Remember to initialize S as below each time before 
##calling parsimonyscore(T)
for i in range(nleaves, nnodes, 1):
	S[i] = ''
score1 = smallparsimony.parsimonyscore(T)	
print(score1)

NNI(T, nnodes-1, 0, nnodes-1)

print(P)
print(L)
print(R)
print(S)

for i in range(nleaves, nnodes, 1):
	S[i] = ''
score2 = smallparsimony.parsimonyscore(T)	
print(score2)

NNI(T, nnodes-1, 0, nnodes-1)

NNI(T, nnodes-1, 1, nnodes-1)

print(P)
print(L)
print(R)
print(S)

for i in range(nleaves, nnodes, 1):
	S[i] = ''
score2 = smallparsimony.parsimonyscore(T)	
print(score2)




#newick_tree = ""
#newick_tree = newick(nnodes-1, newick_tree, L, R)
##print(newick_tree)

#for i = nnodes-1 to nleaves:
#	NNI(T, i, 0, nnodes-1)
#	if(newscore is better then accept change)
#	else(undo change)
#	i = i -1

#Output the besttree

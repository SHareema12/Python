##Functions##
def getMinPair(d):
	minDist = 100000 
	bestI = -1
	bestJ = -1 

	##Get mimDist and bestI and bestJ from matrix-- since the loop 
	### iterates over the diagonal, bestJ will be left child and 
	### bestI will be right child 
	for i in range(0,len(d),1): 
		for j in range(0,len(d),1):
			if(i != j and d[i][j] != 'x'):
				d[i][j] = float(d[i][j])
				if (d[i][j] <= minDist):
					minDist = d[i][j]; 
					bestI = i 
					bestJ = j 
	return [bestI,bestJ] 

def addNewNode(P,L,R,leaves,bestI,bestJ,newNodeID):
	##Updates P, L, and R for new node 
	P[bestI] = newNodeID 
	P[bestJ] = newNodeID
	R[newNodeID] = bestI
	L[newNodeID] = bestJ 
	##Updates leaves with left and right child of new node 
	leaves[newNodeID] = leaves[bestI] + ' ' + leaves[bestJ]
	print(leaves)

	return

def updateMatrix(bestI,bestJ,newNodeID, d, D, leaves, P):
	##Cross out rows and columns after updating distances for new node 
	for i in range(0, len(d)): 
		d[bestJ][i] = 'x'
		d[bestI][i] = 'x'
		d[i][bestI] = 'x'
		d[i][bestJ] = 'x'

	for i in range(0,newNodeID,1): 
		##Whichever node doesn't have a parent is an available node-need to calculate distances
		if (P[i] == -1):
			newDist = distance(i, newNodeID, leaves, D)
			d[newNodeID][i] = newDist
			d[i][newNodeID] = d[newNodeID][i]

	return

def distance(currentNode, newNodeID, leaves, D):
	currNodeLeaves = leaves[currentNode].split()
	newNodeLeaves = leaves[newNodeID].split()

	totalDist = 0
	numLeaves = len(currNodeLeaves) * len(newNodeLeaves)
	sumLeaves = 0
	
	for i in range(0,len(newNodeLeaves),1):
		for j in range(0,len(currNodeLeaves),1):
			newNleaf = int(newNodeLeaves[i])
			currNleaf = int(currNodeLeaves[j])
			cellDist = float(D[newNleaf][currNleaf])
			sumLeaves = sumLeaves + cellDist

	totalDist = sumLeaves/numLeaves

	return totalDist
	

##Main##
#Implementing Distance Based Phylogeny-particularly UPGMA methodology 
#Input: distance matrix, so we need to write code to read the matrix 

##Read distance matrix from file into lists of lists 
data = open("matrix.txt").readlines() 

nleaves = len(data)
print("nleaves:", nleaves)
nnodes = (2*nleaves) -1

nodesToDo = nleaves

D = [] 

print("data", data)

##Another way of reading in data and making normal matrix of leafnodes x leafnodes
for i in range(0, len(data), 1): 
	data[i] = data[i].strip('\n')
	l = data[i].split() 
	for j in range(0,len(l), 1):
		l[i] = (l[j])
	D.append(l) 

for i in range(0,len(D),1):
	for j in range(0,len(D)):
		if (i == j):
			D[i][j] = 0


##Make d[] of dimension nnodes x nnodes 
d = [] 

for i in range(0,nnodes,1):
	l = []
	for j in range(0,nnodes,1): 
		l.append('x')
	d.append(l)

##Initializing the big matrix to the values that are in small matrix
for i in range(0,nleaves,1):
	for j in range(0,nleaves,1):
		d[i][j] = D[i][j]

P = []
L = []
R = []
leaves = []

##Initialize P,L,R,and leaves with default values 
for i in range(0,nnodes,1): 
	P.append(-1)
	L.append(-1)
	R.append(-1)
	leaves.append('')

for i in range(0,nleaves,1):
	leaves[i] = str(i) 

newNodeID = len(D)

for i in range(0, len(d)):
	print(d[i])

##While loop that constructs the tree 
while (nodesToDo > 1):
	print("Iteration for node:", newNodeID)
	bestIJ = getMinPair(d)
	print("BestIJ:", bestIJ[0], bestIJ[1])
	addNewNode(P, L, R,leaves, bestIJ[0], bestIJ[1], newNodeID)
	updateMatrix(bestIJ[0], bestIJ[1], newNodeID, d, D, leaves, P)
	for i in range(0, len(d)):
		print(d[i])
	newNodeID = newNodeID + 1
	nodesToDo = nodesToDo - 1

print()
print("P:", P)
print("L:", L)
print("R:", R)
print("leaves:", leaves) 
import random

import smallparsimony

def randomTgen(data):
    ##taking off ''\n' at the end of each word
    for i in range(0,len(data),1):
        data[i] = data[i].strip('\n')
    
    ##Extract sequences- all even lines of data
    dataArray = []
    for i in range(1,len(data), 2):
        dataArray.append(data[i])
    #print("Sequences:", dataArray)

    ##Declare array containing number of leaf nodes that we will randomize
    items = []
    for i in range(0,len(dataArray),1):
        items.append(i)

    ##Randomize numbers in list to pick
    random.shuffle(items)

    ##Initialize S array, L array, and R array, declare P array
    ##Initialize leafNodes, totalNodes
    P = []
    S = []
    L = []
    R = []

    leafNodes = len(dataArray)
    totalNodes = (2*leafNodes)-1

    ##Initialize S array with sequences first
    for i in range(0,len(dataArray),1):
        S.append(dataArray[i])

    ##Fill rest of S with empty string ''
    for j in range(0, totalNodes-leafNodes, 1):
        S.append('')

    ##Initialize L and R values with -1
    for i in range(0,leafNodes,1):
        L.append(-1)
        R.append(-1)

    ##Initialize remaining spots of L and R with empty strings
    for i in range(0, totalNodes-leafNodes,1):
        L.append('')
        R.append('')

    ##Initialize P with empty string values
    for i in range(0,totalNodes,1):
        P.append('')

    ##Generating Random Tree
    nextPnode = leafNodes

    while(len(items)>1):
        #Arbitrarily pop last two items and make them left and right node 
        nodeL = items.pop()
        nodeR = items.pop()

        #Pop empty value for new node's left child, insert left node
        L.pop(nextPnode)
        L.insert(nextPnode,nodeL)

        #Pop empty value for new node's right child, insert right node
        R.pop(nextPnode)
        R.insert(nextPnode,nodeR)

        #Pop empty value for new node's parent, insert parents for new L and R nodes
        P.pop(nodeL)
        P.insert(nodeL,nextPnode)
        P.pop(nodeR)
        P.insert(nodeR,nextPnode)
        
        #Update items with new node number to make it available for picking
        items.append(nextPnode)
        random.shuffle(items)
        nextPnode += 1

        #print("Nodes being joined:", nodeL, S[nodeL], "and",nodeR, S[nodeR])
        #print("New parent node:", nextPnode-1)
        
    ##Assign last node-aka root's parent as -1
    root = items.pop()
    P.pop(root)
    P.insert(root, -1)

    T = [P,L,R,S]

    return T

def newick(root, newick_tree, L, R):   
    l = L[root]
    r = R[root]
    if l == -1 and r == -1:
#        name = names[root]
        name = data[2*root]
#        s = name.split()
#        name = s[1] + "-" + s[2]
#        name = str(root)
        newick_tree = newick_tree + name
        return newick_tree
    else:
        newick_tree = newick_tree + "("
        newick_tree = newick(l, newick_tree, L, R)
        newick_tree = newick_tree + ","
        newick_tree = newick(r, newick_tree, L, R)
        newick_tree = newick_tree + ")"
        return newick_tree

def NNI(T, root, bestuv):
    P = T[0]
    L = T[1]
    R = T[2]
    S = T[3]

    if (L[root] == -1 and R[root] == -1):
        return T
    
    #otherwise perform NNI on left and right edge below root node
    beforescore = smallparsimony.parsimonyscore(T)

    NNI1Tree = NNI1(T,root)
    NNI2Tree = NNI2(T,root)

    print("NNI1 Tree:", T)
    print("NNI2 Tree:", T)

    NNI1TreeRoot = len(NNI1Tree[0])-1
    NNI2TreeRoot = len(NNI2Tree[0])-1

    NNI1score = smallparsimony.getparsimonyscore(NNI1Tree, NNI1TreeRoot,0)
    NNI2score = smallparsimony.getparsimonyscore(NNI2Tree, NNI2TreeRoot,0) 

    bestscore = 0
    
    if (NNI1score > beforescore and NNI1score > NNI2score):
        T = NNI1Tree
        bestuv[0] = root
        bestuv[1] = L[root]
        bestscore = NNI1score
    elif (NNI2score > beforescore and NNI2score > NNI1score):
        T = NNI2Tree
        bestuv[0] = root
        bestuv[1] = L[root]
        bestscore = NNI2score
        

    print("went thru NNI method yay")
    print("best score thus far:", bestscore)
    
    NNI(T,L[root],bestuv)
    NNI(T,R[root],bestuv)
    
    return T

def NNI1(T,root):
    P=T[0]
    L=T[1]
    R=T[2]
    S=T[3]

    u = root
    v = L[u]
    temp = L[v]
    L[v] = R[u]
    R[u] = temp
    P[L[v]] = u
    P[R[u]] = v

    return T
    
def NNI2(T,root):
    P=T[0]
    L=T[1]
    R=T[2]
    S=T[3]

    u = root
    v = L[u]
    temp = R[v]
    R[v] = R[u]
    R[u] = temp
    P[R[v]] = u
    P[R[u]] = v

    return T
######
##Main
######

f = open("dna.fasta")
data = f.readlines()

T = randomTgen(data)

print("Tree before:")
print(T[0])
print(T[1])
print(T[2])
print(T[3])

root = len(T[0])-1
L = T[1]
R = T[2]

print(T[3])

bestscore = 100000

score = smallparsimony.parsimonyscore(T)

print("Score", score)

'''for i in range(100):
    T = randomTgen(data)
    score = smallparsimony.parsimonyscore(T)
    if (score < bestscore):
        bestscore = score
'''


#print("Best score:", bestscore)

newick_tree = ""
root = len(T[0])-1
L = T[1]
R = T[2] 
#print(newick(root,newick_tree,L,R))

bestuv = [root, L[root]]

bestTree = NNI(T,root,bestuv)
        
    


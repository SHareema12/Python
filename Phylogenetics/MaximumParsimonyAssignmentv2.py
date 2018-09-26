'''Write a Python program to that takes as input a set of aligned
DNA sequences and outputs the maximum parsimony tree as given
by an NNI-based local search. Use the pseudocode below that we 
also discussed in class.
'''
import random 
import smallparsimony

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
    #print("Runs NNI ", root, "th/nd/st time")
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
        #print("u: ", u)
        v = L[u]
        #print("v: ", v)
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

#Read aligned sequences from file in FASTA format
#Make a random tree T

def maxParsUsingNNI(T, rootnode,nleaves,nnodes):
    ##Get initial parsimony score of tree as is before running NNI moves
    bestScore = smallparsimony.parsimonyscore(T)
    done = 0
    while(done != 1):
        for i in range(rootnode, nleaves, -1):
            #print("i: ", i)
            #don't forget to initialize S  
            for j in range(nleaves, nnodes, 1): 
                S[j] = '' 

            ##get initial parsimony score
            score1 = smallparsimony.parsimonyscore(T)
            #print("Initial parsimony score before NNI move: ", score1)

            ##perform first NNI move based on ith node 
            NNI(T, i, 0, rootnode)

            for j in range(nleaves, nnodes, 1):
                S[j] = '' 

            score2 = smallparsimony.parsimonyscore(T)
            #print("Parsimony score after 1st NNI move: ", score2)

            if(score2 < score1 and score2 < bestScore):
                bestScore = score2
                #i = -1
                #break  #exit loop

            elif (score1 < bestScore and score1 < score2):
                bestScore = score1
            ##undo the NNI move we just did
                NNI(T, i, 0, rootnode) 

            #perform NNI on other side 
            NNI(T, i, 1, rootnode)
      
            for j in range(nleaves, nnodes, 1):
                S[j] = '' 

            score2 = smallparsimony.parsimonyscore(T)
            #print("Parsimony Score after 2nd NNI move: ", score2)

            if(score2 < score1 and score2 < bestScore) :
                bestScore = score2
                #i = -1
                #break #exit loop

            else:
            ##undo NNI move we just did, at this point neither of 
            ## NNI moves result in better parsimony score
            ## than the original tree 
                NNI(T, i, 1, rootnode) 

            if(i == nleaves):
                done = 1 #this means we have done one pass
    				   #of the tree without finding a better
        			   #score and so we are done with the search
        done = 1

    return bestScore

#######
###Main
#######

f = open("hemoglob.fasta")
data = f.readlines()

for i in range(0, len(data), 1):
    data[i] = data[i].strip('\n')

nleaves = int(len(data)/2)
print("Nleaves:", nleaves)
nnodes = (2*nleaves) - 1

print("Nnodes: ", nnodes)

P = []
L = []
R = []
S = []
T = [P, L, R, S]
randomtree(T, nnodes, nleaves)

print("Tree:")
print(T[0])
print(T[1])
print(T[2])
print(T[3])


rootnode = len(T[0])-1
#print(nnodes)

bestScore = maxParsUsingNNI(T, rootnode, nleaves, nnodes)

print("Best Parsimony Score: ", bestScore)


#Your completed program is due March 21st 2017 as hardcopy in class. 

#Also submit your program in the directory /afs/cad/courses/bnfo/s17/bnfo/602/002


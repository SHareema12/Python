import random
import smallparsimonyj

f = open("hemoglob.fasta")
data = f.readlines()
for i in range(0, len(data), 1):
    data[i] = data[i].strip('\n')

nleaves = int(len(data)/2)
nnodes = (2*nleaves) - 1

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

######## Random Tree ########
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

######## Nearest Neighbor Interchange (NNI) ########
def NNI(T, root, flag, trueroot):
    P = T[0]
    L = T[1]
    R = T[2]
    S = T[3]

    if(root != trueroot):
        u = root
        v = L[u]
        if(L[v] == -1 and R[v] == -1):
            return
        if(flag == 0):
            temp = L[v]
            L[v] = R[u]
            R[u] = temp
            P[L[v]] = v
            P[R[u]] = u
        elif(flag == -1):
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

P = []
L = []
R = []
S = []
T = [P, L, R, S]

randomtree(T, nnodes, nleaves)
pscore = smallparsimonyj.parsimonyscore(T)
print("Random Tree Parsimony Score: ", pscore)
newick_tree = ""
newick_tree = newick(nnodes-1, newick_tree, L, R)
print("newick tree:", newick_tree)
print("------------------------------------------------------------")

trueroot = nnodes-1
done = 0

while(not(done)):
    for i in range(nleaves, nnodes, 1):
        for j in range(nleaves, nnodes, 1):
            S[j] = ''
        score1 = smallparsimonyj.parsimonyscore(T)
        print("Parsimony score before NNI move: ", score1)

        ### 1st NNI move ###
        NNI(T, i, 0, trueroot)
        for j in range(nleaves, nnodes, 1):
            S[j] = ''
        score2 = smallparsimonyj.parsimonyscore(T)
        print("Parsimony score after first NNI move: ", score2)
        if(score2 < score1):
            minscore = score2
            i = -1
            break
        else:
            minscore = score1
            NNI(T, i , 0, trueroot)

        ### 2nd NNI move ###
        NNI(T, i, 1, trueroot)
        for j in range(nleaves, nnodes, 1):
            S[j] = ''
        score2 = smallparsimonyj.parsimonyscore(T)
        print("Parsimony score after second NNI move: ", score2)
        if(score2 < score1):
            minscore = score2
            i = -1
            break
        else:
            NNI(T, i, 1, trueroot)

        if(i == nnodes-1):
            done = 1

print("------------------------------------------------------------")
print("Maximum Parsimony Score: ",minscore)
newick_tree = ""
newick_tree = newick(nnodes-1, newick_tree, L, R)
print("newick tree:", newick_tree)


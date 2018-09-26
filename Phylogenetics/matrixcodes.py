##### FUNCTIONS ##########
###### def: Find closest pair in d ######
###### Returns indices i and j taht are closest
###### Ignores entries that are non-positives
def get_min_pair(d):
    mindist = 100000000
    best_i = -1
    best_j = -1

    # looking through every cell for shortest distance (with exceptions)
    for i in range(0, len(d), 1):
        for j in range(0, len(d), 1):
            if(i != j and d[i][j] != 'x' and d[i][j] <= mindist):
                mindist = d[i][j]
                best_i = i
                best_j = j
    return [best_i, best_j]


###### def: Add new node in tree ######
###### Parameters are P, L, R, new_node_id and
######## indices i and j from above function
def add_new_node(P, L, R, best_i, best_j):
    P[best_i] = new_node_id
    print(P[best_i])
    P[best_j] = new_node_id
    print(P[best_j])
    L[new_node_id] = best_i
    print(L[new_node_id])
    R[new_node_id] = best_j
    print(R[new_node_id])
    leaves[new_node_id] = leaves[best_i] + ' ' + leaves[best_j]
    print(leaves[new_node_id])


###### def: Update distance matrix d ######
###### Calculate distances from new node to nodes
######## that have parent set to -1
###### Set row and column of nodes i and j
######## (that were returned by find_closest_pair) to -1
def update_matrix(best_i, best_j, new_node_id, d, D, leaves):
    for i in range(0, len(d), 1):
        d[best_j][i] = 'x'
        print(d[best_j][i])
        d[best_i][i] = 'x'
        d[i][best_j] = 'x'
        d[i][best_i] = 'x'

    #for i in range(0, new_node_id, 1):
        #if(P[i] == -1):
            #d[new_node_id][i] = distance(new_node_id, i, leaves, D)

    #d[i][new_node_id] = d[new_node_id][i]


def distance(new_node_id, i, leaves, D):
    l.a = leaves[a].split()
    l.b = leaves[b].split()
    total = 0
    
    for i in range(0, len(l.a), 1):
        for j in range(0, len(l.b), 1):
            total += D[l.a[i]][l.b[j]]

    total = total/(len(l.a)+len(l.b))
    return total


###########################
###########################
##### MAIN CODES ##########
###########################
f = open("matrix")
data = f.readlines()
print(data)

###### Initialization ######
### D has dimensions n x n, where n is the number of sequences (leaves)
D = []

for i in range(0, len(data), 1):
    data[i] = data[i].strip('\n')
    print("strip 'n': ")
    print(data[i])
    data[i] = data[i].split()
    print("spliting a string: ")
    print(data[i])

    for j in range(0, len(data[i]), 1):
        data[i][j] = float(data[i][j])
        print("add decimal: ")
        print(data[i][j])
    D.append(data[i])

print("matrix: ")
for i in range(0, len(D), 1):
    print(D[i])
    
nleaves = len(data)
nnodes = 2*(nleaves)-1
print("number of leaves: ", nleaves)
print("number of nodes: ", nnodes)

### d has dimensions 2n+1
d =[]

for i in range(0, nnodes, 1):
    l = []
    for j in range(0, nnodes, 1):
        if(i == j):
            l.append(0.0)
        else:
            l.append('x')
    d.append(l)

print("giant matrix: ")
for i in range(0, len(d), 1):
    print(d[i])

for i in range(0, nleaves, 1):
    for j in range(0, nleaves, 1):
        d[i][j] = D[i][j]

print("giant matrix: ")
for i in range(0, len(d), 1):
    print(d[i])

### P, L, and R lists
P = []
L = []
R = []
leaves = []

for i in range(0, nnodes, 1):
    P.append(-1)
    L.append(-1)
    R.append(-1)
    leaves.append('')

print("P: ", P)
print("L: ", L)
print("R: ", R)
print("leaves: ", leaves)

for i in range(0, nleaves, 1):
    leaves[i] = str(i)
    print(leaves[i])
print(leaves)

#########################################
#########################################
###### While(nodes_to_do > 1): ##########
###### Find closest pair in distance matrix d: get_min_pair(d)
###### Add new node in tree: add_new_node(P, L, R, best_i, best_j)
###### Update distance matrix: distance(new_node_id, i, leaves, D)
###### nodes_to_do = nodes_to_do - 1

min_pair = get_min_pair(d)
print(min_pair)

#if the new node is 4:
print("if the new node is 4: ")
new_node_id = 4
add_new_node(P, L, R, 1, 0)
print("P: ", P)
print("L: ", L)
print("R: ", R)
print("leaves: ", leaves)

update_matrix(1, 0, 4, d, D, leaves)
print("giant matrix: ")
for i in range(0, len(d), 1):
    print(d[i])

best_i = D[3][0]
print(best_i)

nd = leaves[4].split()
print(nd)


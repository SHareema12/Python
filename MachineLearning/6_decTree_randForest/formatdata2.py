import sys

##################
### Functions ####
##################
def blast_like_alignment_fast(seq1, seq2):
    score=0
    seq2htlist={}
    for i in range(0, len(seq2), 1):
        kmer2=seq2[i:i+3]
        seq2htlist[kmer2]=1
    for i in range(0, len(seq1), 1):
        kmer1=seq1[i:i+3]
        if(seq2htlist.get(kmer1) != None):
            score=score+1
    return score

def obtain_feature_vector(protein, reference):
    fv=[]
    for i in range(0, len(reference), 1):
        fv.append(str(blast_like_alignment_fast(protein, reference[i])))
    return fv

#### Read in reference proteins into a list ####
ref=open("reference.txt")
reference=[]
for line in ref:
    line=line.strip('\n')
    if(line[0] != '>'):
        reference.append(line)

postrain = sys.argv[1]
negtrain = sys.argv[2]
postest = sys.argv[3]
negtest = sys.argv[4]

## Output are full data, full labels, training labels	
data = open("data", "w")
labels = open("labels", "w")
trainlabels = open("trainlabels", "w")

f = open(postrain)
row = 0
sequence = ''
line = f.readline()
for line in f:
    if(line[0] == '>'):
        fv = obtain_feature_vector(sequence, reference)
        fv = ' '.join(fv)
        data.write(fv + '\n')
        labels.write("1 " + str(row) + '\n')
        trainlabels.write("1 " + str(row) + '\n')
        row += 1
        sequence = ''
    else:		
        line = line.strip('\n')
        sequence = sequence + line

f = open(negtrain)
sequence = ''
line = f.readline()
for line in f:
    if(line[0] == '>'):
        fv = obtain_feature_vector(sequence, reference)
        fv = ' '.join(fv)
        data.write(fv + '\n')
        labels.write("0 " + str(row) + '\n')
        trainlabels.write("0 " + str(row) + '\n')
        row += 1
        sequence = ''
    else:
        line = line.strip('\n')
        sequence = sequence + line

f = open(postest)
sequence = ''
line = f.readline()
for line in f:
    if(line[0] == '>'):
        fv = obtain_feature_vector(sequence, reference)
        fv = ' '.join(fv)
        data.write(fv + '\n')
        labels.write("1 " + str(row) + '\n')
        row += 1
        sequence = ''
    else:
        line = line.strip('\n')
        sequence = sequence + line

f = open(negtest)
sequence = ''
line = f.readline()
for line in f:
    if(line[0] == '>'):
        fv = obtain_feature_vector(sequence, reference)
        fv = ' '.join(fv)
        data.write(fv + '\n')
        labels.write("0 " + str(row) + '\n')
        row += 1
        sequence = ''
    else:
        line = line.strip('\n')
        sequence = sequence + line

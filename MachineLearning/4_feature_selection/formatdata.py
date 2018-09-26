import sys

##################
### Functions ####
##################
def obtain_feature_vector(protein, k):

        fv = []
        k = 3
#        dna = ['A','C','G','T']
        prot = [ 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z' ,'X' ]

        for i in range(0, 23**(k), 1):
                firstind = (i // 23**0) % 23
                secondind = (i // 23**1) % 23
                thirdind = (i // 23**2) % 23
                kmer = prot[thirdind]+prot[secondind]+prot[firstind]
                c = protein.count(kmer)
                fv.append(str(c))

        return fv

postrain = sys.argv[1]
negtrain = sys.argv[2]
postest = sys.argv[3]
negtest = sys.argv[4]

##Output are full data, full labels, training labels	
data = open("data", "w")
labels = open("labels", "w")
trainlabels = open("trainlabels", "w")

f = open(postrain)
row = 0
sequence = ''
l = f.readline()
for l in f:
	if(l[0] == '>'):
		fv = obtain_feature_vector(sequence, 3)
		fv = ' '.join(fv)
		data.write(fv + '\n')
		labels.write("1 " + str(row) + '\n')
		trainlabels.write("1 " + str(row) + '\n')
		row += 1
		sequence = ''
	else:		
		l = l.strip('\n')
		sequence = sequence + l

f = open(negtrain)
sequence = ''
l = f.readline()
for l in f:
	if(l[0] == '>'):
		fv = obtain_feature_vector(sequence, 3)
		fv = ' '.join(fv)
		data.write(fv + '\n')
		labels.write("0 " + str(row) + '\n')
		trainlabels.write("0 " + str(row) + '\n')
		row += 1
		sequence = ''
	else:
		l = l.strip('\n')
		sequence = sequence + l

f = open(postest)
sequence = ''
l = f.readline()
for l in f:
	if(l[0] == '>'):
		fv = obtain_feature_vector(sequence, 3)
		fv = ' '.join(fv)
		data.write(fv + '\n')
		labels.write("1 " + str(row) + '\n')
		row += 1
		sequence = ''
	else:
		l = l.strip('\n')
		sequence = sequence + l

f = open(negtest)
sequence = ''
l = f.readline()
for l in f:
	if(l[0] == '>'):
		fv = obtain_feature_vector(sequence, 3)
		fv = ' '.join(fv)
		data.write(fv + '\n')
		labels.write("0 " + str(row) + '\n')
		row += 1
		sequence = ''
	else:
		l = l.strip('\n')
		sequence = sequence + l

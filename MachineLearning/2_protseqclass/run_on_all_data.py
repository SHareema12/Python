import os
import re
import sys 

d = os.listdir('fisher-scop-data')
nmerr = 0 
nberr = 0
n=0 
for i in range(0,len(d),1):
  if(re.match('\d\.\d', d[i]) != None):
    d2 = os.listdir('fisher-scop-data/' + d[i])
    
    #### Get negative train and test #### 
    for j in range(0, len(d2), 1): 
      if(d2[j].find('fold0.neg-train') != -1):
        negtrain = 'fisher-scop-data/' + d[i] + '/' + d2[j]
        negtest = negtrain.replace('train', 'test')
        print("For directory ", d[i], negtrain, negtest) 
    
    #### Descend into subdirectories ####
    for j in range(0, len(d2), 1): 
      if(d2[j].find('fold') == -1): 
        d3 = os.listdir('fisher-scop-data/' + d[i] + '/' + d2[j]) 
        for k in range(0, len(d3), 1): 
          if(d3[k].find('pos-train') != -1): 
            postrain = 'fisher-scop-data/' + d[i] + '/' + d2[j] + '/' + d3[k]
            postest = postrain.replace('train', 'test') 
            print("For directory ", d2[j], negtrain, negtest, postrain, postest)
            os.system('python formatdata.py ' + postrain + ' ' + negtrain + ' ' + postest + ' ' + negtest)
            os.system('python NearestMeans.py data trainlabels > prediction') 
            os.system('python balerror.py labels prediction > errorout') 
            f = open('errorout')
            error = float(f.readline())
            nmerr += error
            os.system('python NaiveBayes.py data trainlabels > prediction')
            os.system('python balerror.py labels prediction > errorout')
            f = open('errorout')
            error = float(f.readline())
            print(d2[j] + ':' + " Naive Bayes error = ", error) 
            nberr += error
            sys.stdout.flush() 
            n += 1

nmerr /= n
nberr /= n
print("Avg nm error=", nmerr) 
print("Avg nb error=", nberr)
sys.stdout.flush() 


import os
import re
import sys 

d = os.listdir('fisher-scop-data-copy')
DTerr = 0 
RFerr = 0
n=0 
for i in range(0,len(d),1):
  if(re.match('\d\.\d', d[i]) != None):
    d2 = os.listdir('fisher-scop-data-copy/' + d[i])
    
    #### Get negative train and test #### 
    for j in range(0, len(d2), 1): 
      if(d2[j].find('fold0.neg-train') != -1):
        negtrain = 'fisher-scop-data-copy/' + d[i] + '/' + d2[j]
        negtest = negtrain.replace('train', 'test')
        print("For directory ", d[i], negtrain, negtest) 
    
    #### Descend into subdirectories ####
    for j in range(0, len(d2), 1): 
      if(d2[j].find('fold') == -1): 
        d3 = os.listdir('fisher-scop-data-copy/' + d[i] + '/' + d2[j]) 
        for k in range(0, len(d3), 1):
          if(d3[k].find('pos-train') != -1): 
            postrain = 'fisher-scop-data-copy/' + d[i] + '/' + d2[j] + '/' + d3[k]
            postest = postrain.replace('train', 'test') 
            print("For directory ", d2[j], negtrain, negtest, postrain, postest)
            os.system('python formatdata2.py ' + postrain + ' ' + negtrain + ' ' + postest + ' ' + negtest)
            os.system('python DecTree.py data trainlabels > predictionDT')
            os.system('python balerror.py labels predictionDT > errorout') 
            f = open('errorout')
            error = float(f.readline())
            DTerr += error 
            os.system('python RandForest.py data trainlabels > predictionRF')
            os.system('python balerror.py labels predictionRF > errorout') 
            f = open('errorout')
            error = float(f.readline())
            RFerr += error
            sys.stdout.flush()
            n += 1
DTerr /= n
RFerr /= n
print("Avg Decision Tree error=", DTerr) 
print("Avg Random Forest error=", RFerr)

sys.stdout.flush() 
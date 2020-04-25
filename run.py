import sys
import os
from scipy.stats import pearsonr
import ranking
import read_write

if __name__=='__main__':  
  word_vec_file = 'cc.en.300.vec'
  word_sim_file = 'en-hi.0-200.txt'
  print('started reading English vectors')
  word_vecs = read_word_vectors(word_vec_file)
  print('Read English word vectors')
  data1=[]
  lst=[]
  a=open(word_sim_file,'r')
  for line in a:
    x,y=line.split()
    lst.append(x)
  fail=0
  for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
      try:
        data1.append(cosine_sim(word_vecs[lst[i]], word_vecs[lst[j]]))
      except:
        fail+=1
  print('failed:',fail)
  data1.sort() # English cosine values (19900)
  
  word_vec_file = 'cc.hi.300.vec'
  word_sim_file = 'en-hi.0-200.txt'
  print('started reading Hindi vectors')
  word_vecs = read_word_vectors(word_vec_file)
  print('Read Hindi word vectors')
  data2=[]
  lst=[]
  a=open(word_sim_file,'r')
  for line in a:
    x,y=line.split()
    lst.append(y)
  fail=0
  for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
      try:
        data2.append(cosine_sim(word_vecs[lst[i]], word_vecs[lst[j]]))
      except:
        fail+=1
  print('failed:',fail)
  data2.sort() # Hindi cosine values

corr, _ = pearsonr(data1, data2)
print('Pearson correlation:',corr)

import sys
import os


if __name__=='__main__':  
  word_vec_file = '/content/drive/My Drive/BTP_files/cc.en.300.vec'
  word_sim_file = '/content/drive/My Drive/BTP_files/en-hi.0-5000.txt'
  print('started')
  word_vecs = read_word_vectors(word_vec_file)
  print('read word vectors')
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
  data1.sort()

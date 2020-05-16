a=open('words','r')
b=open('words_clean','w')
d={}
ind=1
for line in a:
  k=line.split()
  x,y=k[0],k[1]
  if x not in d:
    d[x]=ind
    ind+=1
  if y not in d:
    d[y]=ind
    ind+=1
  s=str(d[x])+' '+str(d[y])+'\n'
  b.write(s)
a.close()
b.close()
print('Total number of words:',ind-1)

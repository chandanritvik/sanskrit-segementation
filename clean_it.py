a=open('LMI_w1000_p1000_s200','r')
b=open('LMI_w1000_p1000_s200_clean','w')
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

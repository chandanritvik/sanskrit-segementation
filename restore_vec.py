p=open('LMI_w1000_p1000_s200','r')
set1=set()
ind=1
lst=[]
for line in p:
  k=line.split()
  x,y=k[0],k[1]
  if x not in set1:
    set1.add(x)
    lst.append(x)
    ind+=1
  if y not in set1:
    set1.add(y)
    lst.append(y)
    ind+=1
  if ind==2935210:
    break
p.close()
print('Running 2ng loop:')
vec=open('english_deep.vec','r')
vec1=open('english_deep_str.vec','w')
next(vec)
vec1.write('2935209 128\n')
for line in vec:
  x,y=line.split(' ',1)
  rep=lst[int(x)-1]
  vec1.write(rep+' '+y)
vec.close()
vec1.close()

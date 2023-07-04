a=int(input())
if a%2==0:
  a-=1
e=[]
count=-1
for i in range(a):
  count+=2
  e.append(count)
print(*e)

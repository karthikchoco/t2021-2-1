dictt={
  1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0
}
a=list(map(int,input().split(",")))
for i in a:
  for j in range(1,10):
    if i%j==0:
      dictt[j]+=1
print(dictt)

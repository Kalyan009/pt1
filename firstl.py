a=int(input())
b=int(input())
c=pow(10,c)
d=a%c
tot=0
while n>0:
  dig=n%10
  tot=tot+dig
  n=n/10
print(tot)

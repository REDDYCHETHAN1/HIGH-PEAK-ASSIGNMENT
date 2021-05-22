n=int(input("Enter no of employes:"))
d={}
f = open('dict.txt', "r")
mytext=""
mytext=f.read()
#print(mytext)
k=[]
k=mytext.split('\n')
for i in range(len(k)):
    (key, val) = k[i].split(':')
    d[key] = int(val)
di = dict( sorted(d.items(),key=lambda item: item[1]))
#print(di)
k=[]
s=[]
for i in di:
    k.append(di[i])
    s.append(i)
#print(k,s)
min1=k[n-1]-k[0]
for i in range(len(k)-n):
    sum1=k[n+i-1]-k[i]
    if min1>sum1:
        min1=sum1
        ind=i
print(min1)
i=ind
for i in range(ind,ind+n):
    print(s[i],": ",k[i])
print("And the difference between the chosen goodie with highest price and the lowest price is",min1)
    
    


import sys
#sys.stdin=open("input.txt","rt")
n, m=map(int,input().split())
a=[0]*(n+m+3)
max=0
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i+j]+=1
for i in range(n+m+1):
    if a[i]>max:
        max=a[i]
for i in range(n+m+1):
    if a[i]==max:
        print(i, end=' ')






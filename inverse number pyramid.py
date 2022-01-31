n=int(input())
s=1
w=2
c=w
for i in range(2,n+2):
    for j in range(s,w):
        c-=1
        print(c,end='')
    print(" ")
    s=w
    w+=i
    c=w 

ls=[]
ls1=[]
for _ in range(int(input())):
        name = input()
        ls1.append(name)
        score = float(input())
        ls.append(score)
v=min(ls)
ls.remove(v)
v1=min(ls)
n1=ls.index(v1)
print(ls1[n1])

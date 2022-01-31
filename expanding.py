def check(ls):
    ls2=([])
    for i in range(len(ls)):
        if(i<len(ls)-1):
            x=ls[i]-ls[i+1]
        if(x<0):
            x=-x
            ls2.append(x)
    for i in range(len(ls2)):
        if(i<len(ls2)-1):
            if(ls[i+1]>ls[i]):
                r=0
            else:
                r=1
                break
        if(r==1):
            return False
        else:
            return True

ls=list(map(int,input().split()))
check(ls)
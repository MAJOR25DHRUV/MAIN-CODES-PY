def see(n):
    real = ""
    copy = n[0]
    n = n[1:]+" "
    k = 1
    for i in n:
        if i != copy:
            real += str(k)+copy
            k = 1
            copy= i
        else:
            k += 1
    return real
num = "1"
n=int(input())
for i in range(n):
    print (num)
    num = see(num)

so here we are just doing timepass and just chilling out and nothing to do what should we do 

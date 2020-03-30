def findTriplets(n,ls):
    ls.sort()
    a,b,count=0,1,0
    i=a+2
    while a<(n-2):
        if ls[a]+ls[b] > ls[i]:
            i+=1
            continue
        elif ls[a]+ls[b] < ls[i]:
            a+=1
            b+=1
            i=a+2
        if ls[a]+ls[b] == i:
            count+=1
            b+=1
    if count!=0:
        print(count)
    else:
        print(-1)
#code
ntst = int(input())
for tst in range(ntst):
    n = int(input())
    ln3 = input()
    ls2 = ln3.split()
    ls = []
    for itm in ls2:
        ls.append(int(itm))   
    findTriplets(n,ls)
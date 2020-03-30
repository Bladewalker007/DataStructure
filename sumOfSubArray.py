def findSum(n, sum, ls): #O(n^2)
    rng = []
    for i in range(n):
        tsum = 0
        for j in range(i,n):
            tsum+=ls[j]
            if tsum == sum:
                rng.append(i+1)
                rng.append(j+1)
                break
        else:
            tsum = 0
        if tsum != 0:
            break
    if len(rng) == 0:
        print(-1)
    else:
        print(*rng)

def findSum2(n, sum, ls): #O(n)
    rng = []
    wsum = 0
    hdr = 0
    for i in range(n):
        wsum+=ls[i]
        while(wsum>sum):
            wsum-=ls[hdr]
            hdr+=1
        if wsum==sum:
            rng.append(hdr+1)
            rng.append(i+1)
            break
    if len(rng) == 0:
        print(-1)
    else:
        print(*rng)
#code
ntst = int(input())
for tst in range(ntst):
    ln2 = input()
    ln3 = input()
    ls1 = ln2.split()
    ls2 = ln3.split()
    n,sum = int(ls1[0]),int(ls1[1])
    ls = []
    for itm in ls2:
        ls.append(int(itm))   
    findSum2(n,sum,ls)
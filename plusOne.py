def plusOne(ls : list):
    num = 0
    ans = []
    for i in ls:
        num = num*10 + i
    num+=1
    while num!=0:
        ans.append(num%10)
        num = num//10
    ans.reverse()
    print(ans)
plusOne([1,2,3,4])
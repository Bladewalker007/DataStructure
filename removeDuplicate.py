ls = [0,0,1,1,1,2,2,3,3,4]
k,i=ls[0],1
while i<len(ls):
    if k==ls[i]:
        print("Del ",ls[i])
        del ls[i]
    if i<len(ls):
        k=ls[i]
    i+=1
print(ls)
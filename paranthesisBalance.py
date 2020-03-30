n = input()
ls = list(n)
stack = []
top = -1
for i in ls:
    if top==-1:
        stack.append(i)
        top+=1
    elif i=='(':
        stack.append(i)
        top+=1
    elif i=='{':
        stack.append(i)
        top+=1
    elif i=='[':
        stack.append(i)
        top+=1
    elif i==')' and stack[top]=='(':
        stack.pop()
        top-=1
    elif i=='}' and stack[top]=='{':
        stack.pop()
        top-=1
    elif i==']' and stack[top]=='[':
        stack.pop()
        top-=1
    else:
        print(False)
        exit()
if top==-1:
    print(True)
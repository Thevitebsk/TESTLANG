i=input(">>")
c=i.split()
cmd=0
s=[]
inp=''
print(c)
while len(c)!=0:
    cmd+=1
    if c[0]=="out":
        print(end=c[1])
        c.pop(0)
        c.pop(0)
    elif c[0]=="note":
        c.pop(0)
        c.pop(0)
    elif c[0]=="in":
        inp=input("input\n")
        c.pop(0)
    elif c[0]=="push":
        if c[1]=="in":
            s.append(inp)
            c.pop(0)
            c.pop(0)
        elif c[1]=="out":
            print(end=s[0])
            c.pop(0)
            c.pop(0)
            s.pop(0)
        elif c[1]=="char":
            s.append(chr(int(c[1])))
            c.pop(0)
            c.pop(0)
        else:
            s.append(c[1])
            c.pop(0)
            c.pop(0)
    else:
        print(f"CMD:{cmd} UNDEFINED COMMAND")
        break

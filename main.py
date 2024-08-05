i=input(">>")
c=i.split()
cmd=0
s=[]
inp=''
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
            print(end=str(s[0]))
            c.pop(0)
            c.pop(0)
            s.pop(0)
        elif c[1]=="char":
            s.append(chr(int(c[2])))
            c.pop(0)
            c.pop(0)
            c.pop(0)
        else:
            s.append(c[1])
            c.pop(0)
            c.pop(0)
    elif c[0]=="op":
        if c[1]=="plus":
            r=int(s[0])+int(s[1])
            s.append(r)
            s.pop(0)
            s.pop(0)
            c.pop(0)
            c.pop(0)
    else:
        print(f"CMD:{cmd} UNDEFINED COMMAND")
        break

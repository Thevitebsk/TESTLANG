i=input(">>")
c=i.split()
cmd=0
s=[]
inp=''
o=[]
if c[0]=="ID":
    c.pop(0)
    c.pop(0)
    while len(c)!=0:
        print(c)
        cmd+=1
        if c[0]=="out":
            if c[1]=="char":
                o.append(chr(int(c[2])))
                c.pop(0)
                c.pop(0)
                c.pop(0)
            else:
                o.append(c[1])
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
                o.append(s[0])
                c.pop(0)
                c.pop(0)
                s.pop(0)
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
        elif c[0]=="end":
            while len(o)>0:
                print(end=str(o[0]))
                o.pop(0)
            break
        else:
            print(f"CMD:{cmd} UNDEFINED COMMAND")
            break
else:
    print("ID REQIERD")

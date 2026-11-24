def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    c1=len(a[0])
    r1=len(a)
    c2=len(b[0])
    r2=len(b)
    if(c1!=r2):
        return -1
    c=[]
    for i in range(r1):
        c.append([])
        # for j in range()

    for i in range(c1):
        for j in range(r1):
            for k in range(r2):
                try:
                    c[j][k]+=a[j][i]*b[i][k]
                except:
                    c[j].append(0)
                    c[j][k]+=a[j][i]*b[i][k]


    

    
    return c
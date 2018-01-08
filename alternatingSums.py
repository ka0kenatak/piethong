def alternatingSums(a):
    z=[0,0]
    print("a =",a)

    while(len(a)>0):
        if(len(a) == 1):
        #return(z[0]=(z[0]+a[0]))
            z[0]=(z[0]+a[0])
            a.pop(0)
            print("z=",z)
        else:
            z[0]=(z[0]+a[0])
            z[1]=z[1]+a[1]
            a.pop(0)
            a.pop(0)
            print("a =",a)
    #return(z)
    print("z final=",z)



#declaration
test1=[50, 60, 60, 45, 70]
test2=[100, 50]
test3=[80]


#function calls
alternatingSums(test1)
alternatingSums(test2)
alternatingSums(test3)

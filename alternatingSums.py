def alternatingSums(a):
    z=[0,0]
    if(len(z) == 1):
        #return(z[0]=(z[0]+a[0]))
        print(z[0]=(z[0]+a[0]))
    else:
        while(len(z)!=2):
            z[0]=(z[0]+a[0])
            z[1]=z[1]+a[1]
            a.pop(0)
            a.pop(1)
        #return(z)
        print(z)






#declaration
test1=[50, 60, 60, 45, 70]
test2=[100, 50]
test3=[80]


#function calls

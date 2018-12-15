def variableName(name):

    print("input name is",name)
    if name[0].isdigit()==True:
        print("False")
        return(False)

    for val in name:
        if (val=="-" or val==" "):
            print("False")
            return(False)
        elif (val.isdigit()==False and val.isalpha()==False and val!="_"):
            print("False")
            return(False)
    print("True")
    return(True)


#Declarations
var1="2asd3"
var2="sadf-234"
var3="asf_daf_13"
var4="234 3"
var5="234]"

#Function calls
variableName(var1)
variableName(var2)
variableName(var3)
variableName(var4)
variableName(var5)

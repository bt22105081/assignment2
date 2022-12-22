#decimal to binary
a = int(input("enter the number : "))
b = int(input("enter the number : "))
def dectobin(n):
    l = []
    while n!=0:
        r =n%2
        l.append(r)
        n = n//2
    l.reverse()
    return(l)

#& operator
print"a = ",dectobin(a)
print"b = ",dectobin(b)
print"a&b = ",dectobin(a&b),"= ",a&b
print''

#| operator
print"a = ",dectobin(a)
print"b = ",dectobin(b)
print"a|b = ",dectobin(a|b),"= ",a|b
print''

#^ operator
print"a = ",dectobin(a)
print"b = ",dectobin(b)
print"a^b = ",dectobin(a^b),"= ",a^b
print''

#bitshift
print"a<<2 = " ,a<<2
print"b<<2 = " ,b<<2
print''

##bitshift
print"a>>2 = " ,a<<2
print"b>>4 = " ,b<<2
print''



    

  


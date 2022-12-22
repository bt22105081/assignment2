s1 = int(input("Enter the first side :"))
s2 = int(input("Enter the second side : "))
s3 = int(input("Enter the third side : "))

def check(a,b,c):
    
    if a>b+c or b>c+a or c>a+b:
        print("Triangle is not possible with given sides")

    else :
        print("Triangle is possible")    

        if a==b and b==c and c==a:
            print("Triangle is Equilateral")

        elif a==b or b==c or c==a:
            print("Triangle is Isoscles")

        else :
            print("Triangle is Scalene")

    

check(s1,s2,s3)        
    


    

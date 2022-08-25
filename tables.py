
table = (lambda x: x*y for y in range(1,11))
num=int(input("Enter the number: "))
for a in range(1,11):
    for z in table:
        print(num,"X",a,"=",z(num))
        a=a+1
        

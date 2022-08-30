#Create a function and ask the user for two inputs and ask what is the operators
def func():
  x=int(input("Enter the num 1 : "))
  y=int(input("Enter the num 2 : "))
  z=input("Choose '+', '-', '*', '/', '%': ")
  if(z=='+'):
    print("Addition :",x+y)
  elif(z=='-'):
    print("Substraction :",x-y)
  elif(z=='*'):
    print("Multiplication :",x*y)
  elif(z=='/'):
    print("Division :",x/y)
  elif(z=='%'):
    print("Remainder :",x%y)

func()

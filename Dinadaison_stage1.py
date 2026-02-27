number1 = int(input("enter the first number :"))
number2 = int(input("enter the second number :"))
operator = input("enter your operator(+,-,*,/):").strip()
if(operator == "+"):
  Result=number1+number2
elif(operator== "-"):
  Result=number1-number2
elif(operator=="*"):
  Result=number1*number2
elif(operator=="/"):
  if (number2 != 0):
    Result=number1/number2
  else:
    print("ERROR : Division by zero is not allowed.")
    Result = None
else:
  print("please enter valid operator")
  Result = None

if (Result != None):
  print("Result =",Result)
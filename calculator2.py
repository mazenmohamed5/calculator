num1=float(input("enter the first number: "))
operator =input("enter th operator: ")
num2=float(input("enter the second number: "))



if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("please choose the right operator")
first_number = input ("Please enter the first number: ")
second_number = input ("Please enter the second number: ")
operator = input("Select an operator (+, -, *. /): ")

if operator == "+":
    result = first_number + second_number

elif operator == "-":
    result = first_number - second_number

elif operator == "*":
    result = first_number * second_number

elif operator == "/":
    result = first_number / second_number

else: 
    print ("Invalid Operator")


print ("Your answer is: ", result)


# Your Student ID:230543009
# Your Name and Surname:Mehmet Tahir Doğu
while True:
    n1 = int(input("Please enter a number: "))
    n2 = int(input("Please enter a number: "))
    operation = input("Select the operation (+, -, *, /):")
    if operation == "+":
        print(f"The result is {n1 + n2}")
    elif operation == "-":
        print(f"The result is {n1 - n2}") 
    elif operation == "*":
        print(f"The result is {n1 * n2}")
    elif operation == "/":
        if n2 == 0:
            print("Error! Division by Zero")
        else:
            print(f"The result is {float(n1 / n2)}")
    else:
        print("Invalid option!")  

    option =input("Do you want to do another calculation?(y/n):")
    if  option.lower() == "n":
        break
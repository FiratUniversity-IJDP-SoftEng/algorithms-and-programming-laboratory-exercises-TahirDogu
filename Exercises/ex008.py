# Your Student ID:
# Your Name and Surname:
number = int(input("Enter the number of rows: "))

for i in range(1, number + 1):
    spaces = ' ' * (number - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
# Your Student ID:230543009
# Your Name and Surname:Mehmet Tahir Doğu
number = int(input("Enter the number of rows: "))

for i in range(1, number + 1):
    spaces = ' ' * (number - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
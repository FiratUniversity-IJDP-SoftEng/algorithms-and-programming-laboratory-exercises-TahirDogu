# Your Student ID:230543009
# Your Name and Surname:Mehmet Tahir Doğu
word = input("Please enter a string: ")
listofWord = set(word)
print("Character frequencies:")
for letter in sorted(listofWord):
    print(f"{letter} : {word.count(letter)}")
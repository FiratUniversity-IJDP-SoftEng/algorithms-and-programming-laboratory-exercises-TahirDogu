# Your Student ID:230543009
# Your Name and Surname:Mehmet Tahir Doğu
list = list(range(1,11))
originalList = list.copy()
originalList2 = []
print(list)
reverseList=sorted(list,reverse=True)
print(reverseList)
list.extend([11,12,13])
print(list)
print(len(list))
deletedNumbers = [1,13]
for deleted in deletedNumbers:
    if deleted in list:
        list.remove(deleted)
print(list)
for evenNumbers in originalList:
    if evenNumbers %2 == 0:
        originalList2.append(evenNumbers)
print(originalList2)
list1 = [1, 2, 3, 4, 5]

list2 = ["A", "B", "C", "D", "E"]

list3 = ['Hola', 1, True, 40.33]

list4 = [1, 2, [3,4,5], 5, 6]


list1.insert(len(list1), 7)
print(list1, sep="")

list1.append(6)
print(list1)

list1.extend([8 , 9, 10])
print(list1, sep=" ")

list2.pop(2)
print(list2, sep=" ")

del list3[0]
print(list3)
print("Empty List")
list = []
print(list)

print("List of numbers")
list =[1,3,4,5,6,5]
print(list)

print("List of strings and accessing using index")

list = ["Sunday", "Monday", "Tuesday", "Wedensday"]

print(list)
print(list[0])
print(list[1])

print("Multidimensional List")
list = [1,2,3, [5,6,7,8]]
print(list[3])
print(list[3][3])

print("\nMixed data types")
list = ["bajarang", 4, 4.5]
print(list)
print("\n Length of the list: len(list) ")
print(len(list))
print("\n adding an element to the list ")
print(list.append(4))
print(list)

print("Range update the list: ")
list2 = []
for i in range(1, 5):
    list2.append(i)
print(list2)

print("Appending two lists list.append(list2)")
print(list.append(list2))
print(list)


print("\n inserting element to the list at given position, insert")
list2.insert(4, 5)
print(list2)
print("\n Extending list with elements to the list")
print(list.extend(list2))
print(list)
print("\n Negative indexing ")
print("-1 is the last element ")
print(list[-1])


print("Removing element from the list")
list.remove(5)
print(list)





# Python Dictionary:
#     Dictionary in python is a unordered collection of data valus, used to store
#  Dictionary with integer keys
Dict = {1: "one", 2: "two", 3: "Three"}
print(Dict)

# Creating a dictionaries with mixed keys

dict2 = {"One": "number", 1: [1,2,3,4,5]}

print(dict2)

dict3 = {}
print(dict3)
dict3[0] = "geeks"
dict3[4] = "for"
dict3[8] = 1

print(dict3)

dict3[2] = 1, 3, 4, 5

print(dict3)


nested_dict = {1: 3, 3: {"one": 1, "two": 3}}
print(nested_dict)
print(nested_dict[3].get("one"))
print(nested_dict.get(1))
# print(nested_dict.pop(3))
# print(nested_dict.pop(3))
# print(nested_dict.popitem())
print(nested_dict)
print(nested_dict.clear())
# print(nested_dict.popitem())
print(nested_dict)

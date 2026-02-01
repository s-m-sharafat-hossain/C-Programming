
# List: List are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

list1 = [5,6,4,3]
print(list1)


# list index start from 0 to n-1
print(list1[2])


# Changeable:
list1 = [3,4,5,5.6,2.4]
print(list1)


# Find list length using len() function.
print(len(list1))


# List Item Data-type:
list1 = [5,6,4]
list2 = ["hamim", 'Munim', "Sharafat"]
list3 = [4, 5, 'hamim', "Munim", True, False]
print(type(list3))
print(type(list1))


#  We can use list() constructor to indicate list data

L = list([12,33,44,'Hamim',True])
print(L)
print(type(L))
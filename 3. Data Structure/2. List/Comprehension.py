                        # List Comprehension:

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

L = ["Apple","Banana","Charry"]
N=[]
for i in L:
    if 'Apple' in i:
        N.append(i)
print(N)


# Using Comprehension: we can write it in one line

N = [i for i in L if "Apple" in i]  # At first i indicate i value store in N.

print(N)


# The Syntax: newlist = [expression for item in iterable if condition == True]

# If condition is False: if "A" != i

N = [i for i in L if "Apple" != i]
print(N)


                           # Iterable

# The iterable can be any iterable object, like a list, tuple, set etc.

#Use range() function to create an iterable.
N = [i for i in range(10)]  #Here store 0 to 9. range is total index number.
print(N)

# Using condition:
N = [i for i in range(10) if i<5]
print(N)    #Store less then 5. 0 to 4


                        # Expression Change
L = ["Hamim",'Munim','Yeamim']
N = [i.upper() for i in L]      #All change in upper case
print(N)


# Change all value of L to "hamim":
N = ["hamim" for i in L]
print(N)


# Use if else:

N = [i if i != "Hamim" else "Orange" for i in L]    #In this case if Hamim in list change to orange.
print(N)


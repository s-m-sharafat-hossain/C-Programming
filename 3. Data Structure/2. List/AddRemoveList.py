                        # Add List

# Insert Items: To insert a new list item, without replacing any of the existing value.

L = [34,54,True,False,45,"Hamim"]
L.insert(2,"Munim")     # here 2 is index where you add your number.
print(L)


# Without index add in last use append()
L.append("Yeamim")
print(L)


# Add 2 list item use + operator
L1 =[33,44,55,66,12]
L2 = ["hamim","Hi","Munim"]
L3 = L1 + L2
print(L3)



# Add 2 list item use extend()
L1 =[33,44,True,False]
L2 = ["hamim","Hi","Munim"]
L1.extend(L2)
print(L1)


                        # Remove List

# Remove specified item: use remove()
L = [34,44,22,True,"hamim",45]
L.remove("hamim")
print(L)


# Remove specific index: use pop() or del
L.pop(3)
print(L)
del L[0]
print(L)


# Clear List: use clear()
L.clear()
print(L)
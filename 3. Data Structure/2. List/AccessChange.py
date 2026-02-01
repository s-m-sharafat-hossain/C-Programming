
# Access Item: using index value I can access individual value from list.

L = [34, 55, 23, True, 34, 22,"Hamim"]
print(L[3])     # index start from 0 and end n-1. n is total number of list value.



# Negative Indexing: it pick value from reverse way.
print(L[-2]) # start from -1. it print 23



# We can fixed our Range of index
print(L[1:3])   #index 1 to 3. print 34 55 23 True
print(L[:3])    #it start from 0 index
print(L[2:])    #it goes to last
print(L[-4:-1])  #Range of negative index


# Check if Item Exists: using "in"
if "Hamim" in L:
    print("Hamim is present")
else:
    print("Not Present")




# Change list Item value: using index number
L[3] = 34
L[-1] = "Munim"
print(L)



# Change a range of item value: 3 value replace with 1 value
L[1:3]=["Hamim",44]
print(L)


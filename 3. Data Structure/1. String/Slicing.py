
# Slicing:
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.



s = "Sharafat Hossain"
print(s[3:8])


#By leaving out the star index, the range will start at the first:
print(s[:8])


#By leaving out the end index, the range will go to the end:
print(s[4:])


# Using negative index we print a string reverse way
print(s[-5:-1])
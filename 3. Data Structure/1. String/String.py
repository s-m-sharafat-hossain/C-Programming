# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# Print String:
print('Hello World')
s = "Hello World"
print(s)


# Multiline String: Use three quote """ """, ''' '''
a = """Lorem ipsum dolor sit abet,
connecter advising edit,
sed do elusion tempo incident
ut labor et dolor magna aqua."""

b = 'Name: S M Sharafat Hossain ' \
'ID: 2312599642 ' \
'Department: ECE '

print(a,b) #b is not multiline


# String are Arrays
a = "Hello World"
print(a[1])


#Looping Trough a String:
for x in "Banana":
    print(x)


# String length:
s = "Sharafat Hossain"
a = len(s)
print(a)


#Check String:
# To check if a certain phrase or character is present in a string, we can use the keyword "in".

text = "Name: Sharafat Hossain"
print("Sharafat" in text)

#Using if
if "Name" in text:
    print("Name is present")


# If not in the text
print("Life" not in text)

#Using if condition
if "life" not in text:
    print("life is not present")


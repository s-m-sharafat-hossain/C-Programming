
#Python has a set of built in methods that you can use on strings.

# Upper Case: use upper() method
a = "hello world"
print(a.upper())


# Lower Case: lower()
a = "Hello World"
print(a.lower())


# Remove Whitespace: Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# use strip()

a = " Hello, World "
print(a.strip())


#Replace: replace string use replace() method
a = "Hello, World"
print(a.replace("He","Je"))


# Split: split() method create a list based on " " or ",". this list we use in array
a = "Sharafat, hossain, Hamim, Munim, Yeamim"
print(a.split(","))
b=a.split(",")
print(b[1]+b[2])



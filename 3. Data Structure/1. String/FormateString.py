
# String Format:  we can use f"Age: {age}"
age = 24
text = f"My age is {age}"
print(text)


# Placeholder and Modifiers: Use f"The price is {price:.2f} taka"
price = 45.564546
txt = f"The price is {price:.2f} taka"
print(txt)


# We can also use some mathematical operation in {}
a = 56.4456
b = 44.545657
print(f"A + B = {a+b:.2f}")
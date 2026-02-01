# Loop through a list: using for

L = [45,33,45,53,'Hamim',"Hi"]
for i in L:
    print(i)


# Loop through index number: use range() and len()
for i in range(len(L)):
    print(L[i])



# Using While loop: use len() function

i=0
while i<len(L):
    print(L[i])
    i = i+1


#Looping Using List Comprehension: this is a shortest syntax of looping
L= [True, False, 'Hi',56,34,32]
[print(i) for i in L]

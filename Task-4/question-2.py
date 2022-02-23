# Question 2 - To print characters at even index of a string

string=input ("Enter the string : ")
print("characters at even_index : ")
for i in range(len(string)):
    if i%2 == 0:
        print(string[i],end="")
print()

# Method 2 - storing characters into an arry
print("Method 2")

string=input("Enter the string : ")
evenindex=[]
for i in range(len(string)):
    if i%2==0:
        evenindex.append(string[i])
print("characters at even_index: ",evenindex)
print()

# Method 3 - using string slice
print("Method 3")

string=input("Enter the string : ")
even_index=slice(0, len(string), 2)
print("characters at even_index: ",string[even_index])

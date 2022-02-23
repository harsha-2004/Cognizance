#Question 5 - To print pyramid pattern

num=int(input("Enter a number : "))
for i in range (0,num+3):
    for j in range(0,num-i+1):
         print(end=" ")
    for j in range(1,num-j+1):
        print("* ",end="")
    print()

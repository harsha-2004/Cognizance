# Question 3 - to print 2dimensional list
#using basic concepts
print("Method 1")

titles=[]
n=int(input("Enter no of columns : "))
m=int(input("Enter no of students : "))
p=[]

for i in range(1,n+1):
      a=input()
      titles.append(a)
print(titles)
p.append(titles)
row=[]
for k in range(n):
    b=input()
    row.append(b)
    p.append(row)
    print(row)
    row=[]
print()
print(p)

for x in p:  
    for i in x:    
        print(i, end = " ")  
    print()

# question 4 - to check wether a number is a palindrome number

#Method 1 - changing int to string & verify
print("Method 1")

num=int(input("Enter a number : "))     
str_form=str(num)                       
def reverse(str):
    string="".join(reversed(str))
    return string
str_reverse= reverse(str_form)          
if(str_reverse==str_form):                      
    print("Number is a palindrome number")
else:
    print("Number is not a palindrome number")
print()
    
# Method  2 - reversing the number and then equating
print("Method 2")

num=int(input("Enter a number : "))
p=num
a=int(0)
s=int(0)
while num>0:
    s=(num%10)
    a=a*10+s
    num=num//10
print(a)
if(p==a):
    print("True")
else:
    print("False")

    

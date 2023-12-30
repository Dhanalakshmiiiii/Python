a=input("Enter the value of a:")
b=input("Enter the value of b:")
temp=a
a=b
b=temp
print("Value of a and b after swapping:")
print("a="+a)
print("b="+b)

a=28
b=35
a,b=b,a
print(a)
print(b)

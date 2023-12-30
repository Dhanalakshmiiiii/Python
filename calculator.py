a=int(input("a:"))
b=int(input("b:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
c=int(input("Enter the choice:"))
if c==1:
  add=a+b
  print("Addition,a+b=",add)
if c==2:
  sub=a-b
  print("Subtraction:",sub)
if c==3:
  mul=a*b
  print("Multiplication:",mul)
if c==4:
  div=a/b
  print("Division:",div)
if c==5:
  mod=a%b
  print("Modulud:",mod)

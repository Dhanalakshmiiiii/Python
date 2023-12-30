num=int(input("Enter a no."))
flag=0
if num==1:
  print("Not a prime")
elif num>1:
  for i in range(2,num):
    if num%i==0:
      flag=1
      break
if flag:
  print(num,"is not a prime no.")
else:
  print(num,"a prime no.")

n=int(input("Enter a number:"))
sum=0
for i in range(1,n):
  if n%i==0:
    sum=sum+i
if sum==n:
  print("Perfect no.")
else:
  print("Not a perfect no.")

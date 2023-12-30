n=int(input("Enter a number:"))
sum=0
temp=n
while temp>0:
  digit=temp%10
  sum+=digit**3
  temp=temp//10
if n==sum:
  print(n,"is an armstrong no.")
else:
  print(n,"not an armstrong no.")

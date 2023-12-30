try:
  n=int(input("Enter a positive integer:"))
  if n<=0:
    raise ValueError("That is a negative number")
except ValueError as e:
  print(e)

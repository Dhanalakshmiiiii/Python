a=[]
print("Square Matrix")
n=int(input("Enter the rows and columns:"))
b={}
a=[[]*n for i in range(n)]
print("\nEnter the elements of matrix:")
for i in range(0,n):
  for j in range(0,n):
    a[i].append(int(input()))
print("\nGiven matrix:\n",a)
for i in range(0,n):
  for j in range(0,n):
    if a[i][j]!=0:
      b[(i,j)]=a[i][j]
print("Dictionary is:",b)

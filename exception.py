f=input("Enter the filename:")
try:
  f1=open(f,"r")
except:
  print("No such file",f)

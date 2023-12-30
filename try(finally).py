try:
  fileptr=open("a.txt","r")
  try:
    fileptr.write("Hi,Hello")
  finally:
    fileptr.close()
    print("file closed")
except:
  print("error")

f1=open("myfile.txt","r")
f2=open("my.txt","r")
d1=f1.read()
d2=f2.read()
d3=open("con.txt","w")
d3.write(d1 + d2)
d3.close()

file=open("con.txt","r")
print(file.read())
print()

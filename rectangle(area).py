class Rect:
  def _init_(self,a,b):
    self.le=a
    self.br=b
  def area(self):
    return self.le*self.br
  def _it_(self,o):
    if self.area()<self.o():
      return True
    else:
      return False
l1=int(input("Length of Rectangle 1:"))
b1=int(input("Breadth of Rectangle 1:"))
l2=int(input("Length of Rectangle 2:"))
b2=int(input("Breadth of Rectangle 2:"))
rect1=Rect(l1,b1)
rect2=Rect(l2,b2)
if rect1<rect2:
  print("Rectangle 2 is greater")
else:
  print("Rectangle 1 is greater")

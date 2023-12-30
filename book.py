class Publisher:
  def _init_(self,name):
    self.name=name
  def display(self):
    print("Name:",self.name)

class Book(Publisher):
  def _init_(self,name,title,author):
    self.title=title
    self.author=author
    super()._init_(name)
  def display(self):
    print("Name:",self.name,",","Title:",self.title,",","Author:",self.author)

class Python(Book):
  def _init_(self,name,title,author,price,no_of_pages):
    self.price=price
    self.noofpages=no_of_pages
    super()._init_(name,title,author)
  def display(self):
    print("Name:",self.name,",","Title:",self.title,",","Author:",self.author,",","Price:",self.price,",","noofpages:",self.no_of_pages)

a=input("Enter the name:")
b=input("Enter the title:")
c=input("Enter the author:")
d=int(input("Enter the price:"))
e=int(input("Enter the no of pages:"))

t=Publisher()
x=Book()
p=Python()
t.display()
x.display()
p.display()

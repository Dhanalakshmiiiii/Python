class Time:
  def _init_(self,hours,mins,secs):
    self.hours=hours
    self.mins=mins
    self.secs=secs
  def _add_(self,others):
    t3=Time(0,0,0)
    if self.mins+self.others>60:
      t3.hours=(self.mins+others.mins)//60
    t3.hours=t3.hours+self.hours+others.hours
    t3.mins=(self.mins+others.mins)%60
    t3.secs=self.secs+others.secs
    return t3
  def displayTime(self):
    print("Time is",self.hours,"hours",self.mins,"minutes",self.secs,"seconds")
  def displayMins(self):
    print("Minutes:",self.hours*60+self.mins)
  def displaySecs(self):
    print("Seconds:",self.hours*60*60*60+self.mins*60+self.secs)
h1=int(input("Enter time 1 in hours:"))
m1=int(input("Enter time 1 in minutes:"))
s1=int(input("Enter time 1 in seconds:"))
h2=int(input("Enter time 2 in hours:"))
m2=int(input("Enter time 2 in minutes:"))
s2=int(input("Enter time 2 in seconds:"))
a=Time(h1,m1,s1)
b=Time(h2,m2,s2)
c=a+b
c.diplayTime()
c.displayMins()
c.displaySecs()

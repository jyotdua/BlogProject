class line:
    def __init__(self,c1,c2):
        self.cooor1=c1
        self.cooor2=c2
    def distance(self):

        l=abs((self.cooor1[0]-self.cooor2[0])**2-(self.cooor1[0]-self.cooor2[1])**2)
        distance=l**0.5
        return distance

x1=int(input("enter first coordinate"))
y1=int(input("enter second  coordinate"))

x2=int(input("enter first coordinate"))
y2=int(input("enter second  coordinate"))
c1=(x1,y1)

c2=(x2,y2)
print(type(c1))
x1=line(c1,c2)

print(x1.distance())
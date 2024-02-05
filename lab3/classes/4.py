class Point():
    def __init__(self):
        self.x = int(input())
        self.y = int(input())
    def show(self):
        print("x = " + str(self.x), "y = " + str(self.y))
    
    def move(self):
        self.x1 = self.x + int(input())
        self.y1 = self.y + int(input())
        
    def dist(self):
        return ((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2) ** 0.5
    
a = Point()
a.show()
a.move()
print (a.dist())
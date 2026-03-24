class circle:
    def __init__(self, raidus):
        self.raidus=int(raidus)

    def perimetre(self):
        return self.raidus * 3.17 * 2
    
    def area(self):
        return 3.17 * self.raidus **2
    
r1=circle(22/7)
print(r1.area())
print(r1.perimetre())
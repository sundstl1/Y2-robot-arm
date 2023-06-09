class xy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return '({}, {})'.format(round(self.x, 2), round(self.y, 2))
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
    
    def setXy(self, x, y):
        self.x = x
        self.y = y
        
    def addXy(self, other):
        self.x += other.getX()
        self.y += other.getY()
    
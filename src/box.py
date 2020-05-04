from coordinates import xy

class BoxException(Exception):
    def __init__(self, message):
        super(BoxException, self).__init__(message)

class Box:
    #Defines the visuals of the movable boxes
    def __init__(self, width, height, position):
        if (isinstance(width, int) and isinstance(height, int)):
            self.width = width
            self.height = height
        else:
            raise BoxException("height and width must be of type int")
        self.setXY(position)
        
    def move(self, position):
        self.position = position
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getXY(self):
        return self.position
    
    def setXY(self, position):
        if (isinstance(position, xy)):
            self.position = position
        else:
            raise BoxException("position must be of type xy")
        
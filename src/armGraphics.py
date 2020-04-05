from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QBrush, QColor, QGraphicsEllipseItem, QRect, QPen, QWidget

from coordinates import xy

class JointGraphicsItem(QtWidgets.QGraphicsEllipseItem):

    def __init__(self, joint):
        # Call init of the parent object
        super(JointGraphicsItem, self).__init__()

        # Do other stuff
        self.joint = joint
        self.overlap = False
        self.box = None
        self.tempBrush = None
        self.text = QtWidgets.QGraphicsSimpleTextItem()
        self.text.setText(str(joint.NumberOfJoints()))
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.setRect(-8,-8 ,16,16)
        self.updatePosition()
        
    def updatePosition(self):
        location = self.joint.EndPosition(xy(350,350))
        x = location.getX()
        y = location.getY()
        self.setPos(x, 700-y)
        self.text.setPos(x-3,700-y-7)
        if (self.box != None):
            self.box.box.setXY(xy(x-350,y-350))        
        
    def grabBox(self):
        if self.overlap:
            overlappedItems = self.collidingItems()
            for item in overlappedItems:
                if (type(item).__name__ == 'BoxGraphicsItem'):
                    boxGraphics = item
                    self.box = boxGraphics
                    self.tempBrush = self.brush()
                    self.setBrush(QBrush(QColor(20,255,20))) 
                    return True
        return False
    
    def releaseBox(self):
        self.setBrush(self.tempBrush)
        self.box = None
    
    def toggleOverlap(self, bool):
        self.overlap = bool
        
class ConnectionGraphicsItem(QtWidgets.QGraphicsLineItem):

    def __init__(self, start, end):
        # Call init of the parent object
        super(ConnectionGraphicsItem, self).__init__()

        self.start = start
        self.end = end
        pen = QPen()
        pen.setWidth(7)
        self.setPen(pen)
        self.updatePosition()
        
    def updatePosition(self):
        start = self.start.EndPosition(xy(350,350))
        end = self.end.EndPosition(xy(350,350))
        self.setLine(start.getX(), 700-start.getY(), end.getX(), 700-end.getY())
        
    
         
        
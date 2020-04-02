from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QBrush, QColor, QGraphicsEllipseItem, QRect, QPen

from coordinates import xy

class JointGraphicsItem(QtWidgets.QGraphicsEllipseItem):

    def __init__(self, joint):
        # Call init of the parent object
        super(JointGraphicsItem, self).__init__()

        # Do other stuff
        self.joint = joint
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.setRect(-5,-5,10,10)
        self.updatePosition()
        
    def updatePosition(self):
        location = self.joint.EndPosition(xy(350,350))
        self.setPos(location.getX(), 700-location.getY())
        
class ConnectionGraphicsItem(QtWidgets.QGraphicsLineItem):

    def __init__(self, start, end):
        # Call init of the parent object
        super(ConnectionGraphicsItem, self).__init__()

        self.start = start
        self.end = end
        pen = QPen()
        pen.setWidth(5)
        self.setPen(pen)
        self.updatePosition()
        
    def updatePosition(self):
        start = self.start.EndPosition(xy(350,350))
        end = self.end.EndPosition(xy(350,350))
        self.setLine(start.getX(), 700-start.getY(), end.getX(), 700-end.getY())
        
    
         
        
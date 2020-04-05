from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QBrush, QColor, QGraphicsEllipseItem, QRect, QPen, QWidget

from coordinates import xy
from PyQt5.QtWidgets import QToolTip

class JointGraphicsItem(QtWidgets.QGraphicsEllipseItem):

    def __init__(self, joint):
        # Call init of the parent object
        super(JointGraphicsItem, self).__init__()

        # Do other stuff
        self.joint = joint
        self.text = QtWidgets.QGraphicsSimpleTextItem()
        self.text.setText(str(joint.NumberOfJoints()))
        self.setToolTip("test")
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.setRect(-8,-8 ,16,16)
        self.updatePosition()
        
    def updatePosition(self):
        location = self.joint.EndPosition(xy(350,350))
        x = location.getX()
        y = 700-location.getY()
        self.setPos(x, y)
        self.text.setPos(x-3,y-7)
        
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
        
    
         
        
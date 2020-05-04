from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QBrush, QColor, QGraphicsRectItem, QRect, QPen, QWidget

from coordinates import xy

class BoxGraphicsItem(QtWidgets.QGraphicsRectItem):
    
    #Defines the visuals of boxes
    def __init__(self, box):
        # Call init of the parent object
        super(BoxGraphicsItem, self).__init__()
        self.box = box
        brush = QtGui.QBrush(QColor(0,0,255),1) # 1 for even fill
        self.setBrush(brush)
        self.setRect(-1*box.width/2,-1*box.height/2 ,box.width,box.height)
        self.setTransformOriginPoint(self.box.getHeight()/2, self.box.getWidth()/2)
        self.setZValue(-1)
        self.updatePosition()
        
    def updatePosition(self):
        self.setPos(350 + self.box.position.getX(),700 - (350 + self.box.position.getY()))
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

class jointSlider(QtWidgets.QSlider):
   def __init__(self, joint):
       
      super(jointSlider, self).__init__()
      
      self.joint = joint
      self.setOrientation(Qt.Horizontal)
      self.setMinimum(0)
      self.setMaximum(360)
      self.setValue(joint.angle)
      self.setTickPosition(QtWidgets.QSlider.TicksBelow)
      self.setTickInterval(20)
      self.valueChanged.connect(self.valuechange)

   def valuechange(self):
      self.joint.changeAngle(self.value())
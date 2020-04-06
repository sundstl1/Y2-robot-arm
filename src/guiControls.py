import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSpinBox

class jointSlider(QtWidgets.QWidget):
   
   def __init__(self, joint):
       
      super(jointSlider, self).__init__()
      
      self.joint = joint
      self.slider = QtWidgets.QSlider()
      self.slider.setOrientation(Qt.Horizontal)
      self.slider.setMinimum(0)
      #hack for float conversion
      self.slider.setMaximum(36000)
      self.slider.setValue(joint.angle*100)
      self.slider.setStyleSheet(
      "QSlider::groove:horizontal{ \
      border: 1px solid; \
      height: 2px; \
      margin: 0px; \
      }\n"
      "QSlider::handle:horizontal { \
      background-color: orange; \
      border: 1px solid; \
      height: 10px; \
      width: 16px; \
      margin: -5px 0px; \
      }" )
    
      self.numBox = QtWidgets.QDoubleSpinBox()
      self.numBox.setMinimum(0)
      self.numBox.setMaximum(360)
      self.numBox.setValue(joint.angle)
      self.numBox.setMaximumWidth(80)
      self.numBox.setSingleStep(0.01)
      
      self.jointNumber = QtWidgets.QLabel()
      self.jointNumber.setText(" joint " + str(joint.NumberOfJoints()-1) + ":")
      
      layout = QtWidgets.QHBoxLayout(self)
      self.setMaximumHeight(20)
      layout.addWidget(self.jointNumber)
      layout.addWidget(self.numBox)
      layout.addWidget(self.slider)
      
      layout.setContentsMargins(0, 0, 0, 0)
      
      self.slider.valueChanged.connect(self.sliderValueChange)
      self.numBox.valueChanged.connect(self.numBoxValueChange)

   def sliderValueChange(self, value):
      self.joint.changeAngle(float(value)/100)
      self.numBox.setValue(float(value)/100)
      
   def numBoxValueChange(self, value):
       self.joint.changeAngle(value)
       self.slider.setValue(int(value*100))
       
class GrabButton(QtWidgets.QPushButton):
   
   def __init__(self, jointGraphics):
       
      super(GrabButton, self).__init__()
      self.setCheckable(True)
      self.setText("Grab")
      self.jointGraphics = jointGraphics
      
      self.clicked.connect(self.buttonPress)
      
   def buttonPress(self):
       if (not self.isChecked()):
           self.jointGraphics.releaseBox()
           self.setText("Grab")
       else:
            if (self.jointGraphics.grabBox() == False):
                self.setChecked(False)
            else:
                self.setText("Release")
           
           
        
    
    
    
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.Qt import QSpinBox, QFileDialog
from commandImporter import *
from commandExecuter import *
import threading

#The jointslider consists of a slider and a number box, linked together, as well as a label with a joint identifier.
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
      
      #Set custom slider style sheet.
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
      self.jointNumber.setText(" joint " + str(joint.NumberOfJoints()) + ":")
      
      #store slider, number box and label in a layout.
      layout = QtWidgets.QHBoxLayout(self)
      self.setMaximumHeight(20)
      layout.addWidget(self.jointNumber)
      layout.addWidget(self.numBox)
      layout.addWidget(self.slider)
      layout.setContentsMargins(0, 0, 0, 0)
      
      #Connect numberboxes and sliders so their changes match.
      self.slider.valueChanged.connect(self.sliderValueChange)
      self.numBox.valueChanged.connect(self.numBoxValueChange)
      self.setMaximumHeight(100)

   def sliderValueChange(self, value):
      self.joint.changeAngle(float(value)/100)
      self.numBox.setValue(float(value)/100)
      
   def numBoxValueChange(self, value):
       self.joint.changeAngle(value)
       self.slider.setValue(int(value*100))
       
   def updateValue(self):
       #its enough to update just one
       self.numBoxValueChange(self.joint.setAngle)
       
#Defines the button used to grab boxes.       
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

#Defines the button for importing a file.           
class ImportButton(QtWidgets.QPushButton):
    def __init__(self, runButton):
       
      super(ImportButton, self).__init__()
      self.runButton = runButton
      self.setCheckable(False)
      self.setText("Import program")
      
      self.clicked.connect(self.buttonPress)
      
    def buttonPress(self):
        fname = QFileDialog.getOpenFileName(self, 'Select command file', 
         'c:\\',"csv files (*.csv)")
        
        if (fname):
            try:
                reader = CommandCsvReader()
                reader.load(fname[0], ';')
                self.runButton.setReader(reader)
            except:
                #invalid file. No error message for the user yet :(
                pass
            
#Defines the button for running the imported program.
class RunProgramButton(QtWidgets.QPushButton):
    def __init__(self, arm, gui):
       
      super(RunProgramButton, self).__init__()
      self.setCheckable(False)
      self.setEnabled(False)
      self.setText("Run program")
      self.running = False
      self.clicked.connect(self.buttonPress)
      self.reader = None
      self.arm = arm
      
      self.executer = CommandExecuter(self.arm, gui)
      
    def buttonPress(self):
        if (self.running):
            self.stop()
        else:
            self.setText("Stop program")
            self.running = True
            self.executer.setCommands(self.reader.getCommandList())
            thread = threading.Thread(target=self.executer.run)
            thread.start()
            thread2 = threading.Thread(target=self.threadWaiter, args=[thread])
            thread2.start()
            
    # waits for all commands to finish, then sets the button back to "run"       
    def threadWaiter(self, thread):
       thread.join()
       self.setText("Run program")
       self.running = False
        
    def setReader(self, reader):
        self.reader = reader
        self.setEnabled(True)
        
    #stops command execution
    def stop(self):
        self.setText("Run program")
        self.running = False
        self.executer.stop()
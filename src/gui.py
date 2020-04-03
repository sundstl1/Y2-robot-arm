from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QBrush, QColor, QVBoxLayout, QGroupBox

from armGraphics import JointGraphicsItem
from armGraphics import ConnectionGraphicsItem
from coordinates import xy
from guiControls import jointSlider

class GUI(QtWidgets.QMainWindow):
    '''
    The class GUI handles the drawing of a RobotWorld and allows user to
    interact with it.
    '''
    def __init__(self, arm):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.vertical = QtWidgets.QVBoxLayout() # Vertical main layout
        self.centralWidget().setLayout(self.vertical)
        self.label = QtWidgets.QLabel()
        self.vertical.addWidget(self.label)
        self.arm = arm
        self.jointGraphics = []
        self.connectionGraphics = []
        self.jointSliders = []
        self.initWindow()
        self.addConnectionGraphicsItems()
        self.addJointGraphicsItems()
        
        self.addJointSliders()
        
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateScene)
        self.timer.start(10) # Milliseconds
        
    def closeEvent(self, *args, **kwargs):
        self.arm.close()
        return QtWidgets.QMainWindow.closeEvent(self, *args, **kwargs)
        
    def initWindow(self):
        '''
        Sets up the window.
        '''
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('robotArm')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.vertical.addWidget(self.view)
    
    def addJointGraphicsItems(self):
        brush1 = QBrush(QColor(111,111,111))
        brush2 = QBrush(QColor(0,255,0))
        brush3 = QBrush(QColor(255,0,0))
        joint = self.arm
        if (not joint.IsEmpty()):
            jointGraphic = JointGraphicsItem(joint)
            jointGraphic.setBrush(brush3)
            self.jointGraphics.append(jointGraphic)
            self.scene.addItem(jointGraphic)
            joint = joint.tail
        while (not joint.IsEmpty()):
            jointGraphic = JointGraphicsItem(joint)
            jointGraphic.setBrush(brush1)
            self.jointGraphics.append(jointGraphic)
            self.scene.addItem(jointGraphic)
            joint = joint.tail
        #Once more for the root joint
        jointGraphic = JointGraphicsItem(joint)
        jointGraphic.setBrush(brush2)
        self.jointGraphics.append(jointGraphic)
        self.scene.addItem(jointGraphic)
        
    def updateJoints(self):
        for jointGraphic in self.jointGraphics:
            jointGraphic.updatePosition()
            
    def addConnectionGraphicsItems(self):
        startJoint = self.arm
        while (not startJoint.IsEmpty()):
            endJoint = startJoint.tail
            connectionGraphic = ConnectionGraphicsItem(startJoint, endJoint)
            self.connectionGraphics.append(connectionGraphic)
            self.scene.addItem(connectionGraphic)
            startJoint = endJoint
    
    def updateConnections(self):
        for connectionGraphic in self.connectionGraphics:
            connectionGraphic.updatePosition()
    
    def addJointSliders(self):
        joint = self.arm
        controlBox = QGroupBox("Controls")
        self.vertical.addWidget(controlBox)
        vbox = QVBoxLayout()
        controlBox.setLayout(vbox)
        
        
        while (not joint.IsEmpty()):
            slider = jointSlider(joint)
            self.jointSliders.append(slider)
            vbox.addWidget(slider)
            joint = joint.tail
        vbox.addWidget(slider)

    def updateLabel(self):
        self.label.setText("grabber location: " + str(self.arm.EndPosition(xy(0, 0))))
    
    def updateScene(self):
        self.updateJoints()
        self.updateConnections()
        self.updateLabel()
             
            
        
        
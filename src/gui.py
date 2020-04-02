from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QBrush, QColor
from armGraphics import JointGraphicsItem
from armGraphics import ConnectionGraphicsItem
from coordinates import xy

class GUI(QtWidgets.QMainWindow):
    '''
    The class GUI handles the drawing of a RobotWorld and allows user to
    interact with it.
    '''
    def __init__(self, arm):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout() # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.arm = arm
        self.jointGraphics = []
        self.connectionGraphics = []
        self.initWindow()
        self.addJointGraphicsItems()
        self.addConnectionGraphicsItems()
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateScene)
        self.timer.start(100) # Milliseconds
        
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
        self.horizontal.addWidget(self.view)
    
    def addJointGraphicsItems(self):
        brush1 = QBrush(QColor(255,0,0))
        brush2 = QBrush(QColor(0,255,0))
        joint = self.arm
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
            
    def updateScene(self):
        self.updateJoints()
        self.updateConnections()
             
            
        
        
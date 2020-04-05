import sys
import time
import threading
from PyQt5.QtWidgets import QApplication

from arm import Arm
from joint import Joint
from joint import Empty
from gui import GUI
from guiControls import jointSlider
from box import Box
from coordinates import xy

def main():
    #add or remove lines like this to add or remove joints to arm.
    #joint takes parameters: Joint(jointLength, initialAngle)
    #angles are given in degrees
    arm = Joint(50, 0, Empty())
    arm = Joint(40, 30, arm)
    arm = Joint(20, 0, arm)
    arm = Joint(70, -50, arm)
    arm = Joint(30, 0, arm)
    arm = Joint(60, 20, arm)
    arm = Joint(40, 0, arm)
    arm = Joint(20, 0, arm)
    
    boxes = []
    boxes.append(Box(20,20,xy(-4,316)))
    boxes.append(Box(15,20,xy(40,100)))
    boxes.append(Box(30,10,xy(-40,150)))
    
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI(arm, boxes)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

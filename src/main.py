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

def main(armLengths):
    #parses command line arguments to create the arm
    armLengths.pop(0)
    if (len(armLengths) == 0):
        print("Please provide at least one arm length as a command line parameter")
        quit()
    try:
        arm = Joint(float(armLengths.pop(0)), 0, Empty())
        for length in armLengths:
                arm = Joint(float(length), 0, arm)
    except:
        raise Exception("all arguments must be numbers")
    
    #adding movable boxes    
    boxes = []
    boxes.append(Box(20,20,xy(-4,316)))
    boxes.append(Box(15,20,xy(40,100)))
    boxes.append(Box(30,10,xy(-40,150)))
    
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI(arm, boxes)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)

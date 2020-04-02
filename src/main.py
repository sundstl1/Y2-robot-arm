import sys
import time
import threading
from PyQt5.QtWidgets import QApplication

from arm import Arm
from joint import Joint
from joint import Empty
from gui import GUI
from guiControls import jointSlider

def main():
    joint1 = Joint(50, 0, Empty())
    joint2 = Joint(40,0, joint1)
    arm = Joint(20,0, joint2)
    arm = Joint(70, 0, arm)
    arm = Joint(20, 0, arm)
    arm = Joint(20, 0, arm)
    arm = Joint(20, 0, arm)
    arm = Joint(20, 0, arm)
    
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI(arm)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

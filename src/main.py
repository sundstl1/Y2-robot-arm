import sys
import time
import threading
from PyQt5.QtWidgets import QApplication

from arm import Arm
from joint import Joint
from joint import Empty
from gui import GUI

def main():
    joint1 = Joint(50, 0, Empty())
    joint2 = Joint(120,30, joint1)
    arm = Joint(150,50, joint2)
    
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI(arm)
    t = threading.Thread(target=waitTask, args=(arm,))
    
    t.start()
    sys.exit(app.exec_())

def waitTask(arm):
    time.sleep(5)
    arm.tail.changeAngle(120)
    arm.tail.changeLength(70)

if __name__ == '__main__':
    main()

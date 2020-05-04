from commandImporter import *
import threading

class CommandExecuter():
    # This class executes a list of arm commands at specified time stamps.
    # All timestamps are relative i.e. are executed timestamp seconds after run has been called. 
    def __init__(self, arm, gui):
        self.commands = None
        self.arm = arm
        self.gui = gui
        self.RUNNING = False
        self.executeList = []
    
    def getCommands(self):
        if (self.commands == None):
            return []
        else:
            return self.commands
    
    def setCommands(self, commands):
        self.commands = commands
    
    def getTimeCommands(self, time):
        return self.commands.get(time, [])
    
    def executeCommand(self, command):
        if (command.getGrab()):
            self.gui.grabButton.click()
        joint = self.arm.ReverseNthJoint(command.getJoint())
        joint.changeAngle(command.getAngle())
        self.gui.updateControls()
    
    def run(self):
        if (self.commands == None):
            return
        else:
            if (self.RUNNING):
                raise Exception("Already running")
            self.RUNNING = True
            keyList = self.getCommands()
            
            for timestamp in keyList:
                for command in self.commands[timestamp]:
                    t = threading.Timer(timestamp, self.executeCommand, [command])
                    self.executeList.append(t)
                    t.start()
            for t in self.executeList:
                t.join()
            self.RUNNING = False
    
    def stop(self):
        self.RUNNING = False
        for thread in self.executeList:
            thread.cancel()
        self.executeList = []
        
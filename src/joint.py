from arm import Arm
from arm import ArmException
from coordinates import xy
import math
import threading
import time

class Empty(Arm):
    '''A singleton representing the empty list'''

    __instance = None

    def __new__(cls):
        '''Creates a new singleton, if there is none. Returns the singleton.'''
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.name = "Empty"
        return cls.__instance

    def IsEmpty(self):
        return True

    def NumberOfJoints(self):
        return 0

    def NthJoint(self, n):
        '''
        Returns the nth joint in an arm, counting from zero.
        Raises exception ArmException, if self is empty.
        '''
        raise ArmException("arm empty")

    def TrueAngle(self):
        return 0
    
    def EndPosition(self, previousPosition):
        return previousPosition
    
    def __repr__(self):
        return 'Empty()'

    def changeAngle(self, angle):
        raise ArmException("empty arm has no angle")
    
    def changeLength(self, length):
        raise ArmException("empty arm has no length")
    
    def close(self):
        return

class Joint(Arm):

    def __init__(self, length, angle, tail):
        if not isinstance(tail, Arm):
            raise LinkedListException('Cannot construct a Joint using {} as the tail'.format(tail))
        self.length = length
        self.angle = angle
        self.setAngle = angle
        self.tail = tail
        self.RUNNING = True
        
        thread = threading.Thread(target=self.angleUpdater)
        thread.start()
        

    def IsEmpty(self):
        return False

    def NumberOfJoints(self):
        return self.tail.NumberOfJoints() + 1

    def NthJoint(self, n):
        '''
        returns the nth joint.
        '''
        if n == 0:
            return self
        else:
            return self.tail.NthJoint(n-1)
    
    def TrueAngle(self):
        trueAngle = self.angle + self.tail.TrueAngle()
        
        '''
        set angle in the range 0-360.
        '''
        while (trueAngle > 360):
            trueAngle -= 360
        while (trueAngle < 0):
            trueAngle += 360
        return trueAngle
    
    def EndPosition(self, previousPosition):
        angle = math.radians(self.TrueAngle())
        position = xy(self.length * math.sin(angle), self.length * math.cos(angle))
        position.addXy(previousPosition)
        return self.tail.EndPosition(position)

    def __repr__(self):
        return 'Joint(length: {}, angle: {}, setAngle: {}, tail: {})'.format(self.length, self.angle, self.setAngle, self.tail)
    
    def changeAngle(self, angle):
        self.setAngle = angle
    
    def changeLength(self, length):
        self.length = length
        
    def close(self):
        #This function closes all joint threads
        self.RUNNING = False
        self.tail.close()
        
    def angleUpdater(self):
        while self.RUNNING:
            time.sleep(0.01)
            
            #Make sure each joint takes the shortest route
            difference = self.angle - self.setAngle
            if (difference > 180):
                difference -= 360
            elif (difference < -180):
                difference += 360
                
            if (difference == 0):
                #no change neeeded
                continue
            elif (difference > 0):
                change = min(difference, 0.1)
            else:
                change = max(difference, -0.1)
            self.angle -= change
            
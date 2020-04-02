from arm import Arm
from arm import ArmException
from coordinates import xy
import math

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
        return -90
    
    def EndPosition(self, previousPosition):
        return previousPosition
    
    def __repr__(self):
        return 'Empty()'


class Joint(Arm):

    def __init__(self, length, angle, tail):
        if not isinstance(tail, Arm):
            raise LinkedListException('Cannot construct a Joint using {} as the tail'.format(tail))
        self.length = length
        self.angle = angle
        self.setAngle = angle
        self.tail = tail

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
        position = xy(self.length * math.cos(angle), self.length * math.sin(angle))
        position.addXy(previousPosition)
        return self.tail.EndPosition(position)

    def __repr__(self):
        return 'Joint(length: {}, angle: {}, setAngle: {}, tail: {})'.format(self.length, self.angle, self.setAngle, self.tail)
    
    def changeAngle(self, angle):
        self.angle = angle
    
    def changeLength(self, length):
        self.length = length    
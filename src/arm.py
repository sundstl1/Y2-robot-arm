class ArmException(Exception):
    def __init__(self, message):
        super(ArmException, self).__init__(message)

class Arm:
    '''
    A linked list is either empty or a list cell, which
    has a value and a link to another linked list, the 'tail' of the list.
    This is an abstract class; you cannot make any direct
    instances of it. Use Cell or Empty instead.
    Most of the methods are implemented in subclasses.
    '''

    def IsEmpty(self):
        '''Returns true, if the arm has no joints, otherwise false'''
        pass

    def NumberOfJoints(self):
        '''Returns the number of joints in the arm.'''
        pass

    def NthJoint(self, n):
        '''
        Returns the nth joint in an arm, counting from zero.
        Raises exception ArmException, if self is empty.
        '''
        pass
    
    def EndPosition(self):
        '''
        returns the position of the end of the arm
        '''
import unittest
import math

from arm import Arm
from joint import Joint
from joint import Empty
from arm import ArmException
from coordinates import xy

class Coordinate_test(unittest.TestCase):
    def testGet(self):
        coordinate = xy(5,4)
        
        self.assertEqual(5, coordinate.getX())
        self.assertEqual(4, coordinate.getY())
        
    def testSet(self):
        coordinate1 = xy(5,4)
        coordinate1.setX(3)
        coordinate2 = xy(3,6)
        coordinate2.setY(20)
        coordinate3 = xy(2,7)
        coordinate3.setXy(55,65)
        
        self.assertEqual(3, coordinate1.getX())
        self.assertEqual(20, coordinate2.getY())
        
        self.assertEqual(55, coordinate3.getX())
        self.assertEqual(65, coordinate3.getY())
        
    def testAdd(self):
        coordinate = xy(8,12)
        coordinate.addXy(xy(10,11))
        
        self.assertEqual(18, coordinate.getX())
        self.assertEqual(23, coordinate.getY())

class Joint_Test(unittest.TestCase):
    
    def testIsEmpty(self):
        emptyJoint = Empty()
        joint = Joint(5,0,emptyJoint)

        self.assertTrue(emptyJoint.IsEmpty())
        self.assertFalse(joint.IsEmpty())
        
    def testNumberOfJoints(self):
        emptyJoint = Empty()
        joint = Joint(1,0,emptyJoint)
        joint = Joint(2,0,joint)
        joint = Joint(3,0,joint)
        joint = Joint(4,0,joint)
        
        self.assertEqual( 0, emptyJoint.NumberOfJoints())       
        self.assertEqual( 4, joint.NumberOfJoints())
        
    def testNthJoint(self):
        emptyJoint = Empty()
        joint4 = Joint(1,0,emptyJoint)
        joint = Joint(2,0,joint4)
        joint = Joint(3,0,joint)
        joint = Joint(4,0,joint)
        joint = Joint(5,0,joint)
        
        exception = False
        try:
            joint.NthJoint(5)
        except ArmException:
            exception = True
            
        self.assertEqual(joint4, joint.NthJoint(4))
        self.assertTrue(exception)
        
    def testTrueAngle(self):
        emptyJoint = Empty()
        joint1 = Joint(55,55,emptyJoint)
        joint2 = Joint(14,14,joint1)
        joint3 = Joint(-12,-12,joint2)
        joint4 = Joint(288,288,joint3)
        joint5 = Joint(288,288,joint4)
        
        self.assertEqual(288-12+14+55+288-360, joint5.TrueAngle())
        
    def testEndPosition(self):
        emptyJoint = Empty()
        position = xy(0,0)
        joint1 = Joint(4,30,emptyJoint)
        joint2 = Joint(5,-20,joint1)
        joint3 = Joint(3,47,joint2)
        joint4 = Joint(2,80,joint3)
        joint5 = Joint(3,195,joint4)
        endPosition = joint5.EndPosition(position)
        
        self.assertEqual(11.208, round(endPosition.getX(), 3))
        self.assertEqual(5.340, round(endPosition.getY(), 3))
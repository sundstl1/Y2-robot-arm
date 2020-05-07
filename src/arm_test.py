import unittest
import math

from arm import Arm, ArmException
from gui import GUI
from joint import Joint, Empty
from coordinates import xy
from box import Box, BoxException
from commandImporter import ArmCommand, CommandCsvReader
from commandExecuter import *

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
        
        joint.close()
        
    def testNumberOfJoints(self):
        emptyJoint = Empty()
        joint = Joint(1,0,emptyJoint)
        joint = Joint(2,0,joint)
        joint = Joint(3,0,joint)
        joint = Joint(4,0,joint)
        
        self.assertEqual( 0, emptyJoint.NumberOfJoints())       
        self.assertEqual( 4, joint.NumberOfJoints())
        
        joint.close()
        
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
        
        joint.close()
        
    def testReverseNthJoint(self):
        emptyJoint = Empty()
        joint1 = Joint(1,0,emptyJoint)
        joint2 = Joint(2,0,joint1)
        joint3 = Joint(3,0,joint2)
        joint4 = Joint(4,0,joint3)
        joint5 = Joint(5,0,joint4)
        
        self.assertEqual(joint5.ReverseNthJoint(1), joint1, "function returned wrong joint")
        self.assertEqual(joint5.ReverseNthJoint(5), joint5, "function returned wrong joint")
        self.assertEqual(joint5.ReverseNthJoint(3), joint3, "function returned wrong joint")
        
        exception = False
        try:
            joint5.ReverseNthJoint(6)
        except ArmException:
            exception = True
        
        self.assertTrue(exception, "n larger than arm length did not raise exception")
        
        joint5.close()
        
    def testTrueAngle(self):
        emptyJoint = Empty()
        joint1 = Joint(55,55,emptyJoint)
        joint2 = Joint(14,14,joint1)
        joint3 = Joint(12,-12,joint2)
        joint4 = Joint(288,288,joint3)
        joint5 = Joint(288,288,joint4)
        
        self.assertEqual(288-12+14+55+288-360, joint5.TrueAngle())
        
        joint5.close()
        
    def testEndPosition(self):
        emptyJoint = Empty()
        position = xy(0,0)
        joint1 = Joint(4,30,emptyJoint)
        joint2 = Joint(5,-20,joint1)
        joint3 = Joint(3,47,joint2)
        joint4 = Joint(2,80,joint3)
        joint5 = Joint(3,195,joint4)
        endPosition = joint5.EndPosition(position)
        
        self.assertEqual(11.208, round(endPosition.getY(), 3))
        self.assertEqual(5.340, round(endPosition.getX(), 3))
        
        joint5.close()
        
    def testBox(self):
        box = Box(5,10,xy(100,200))
        
        self.assertEqual(5, box.getWidth())
        self.assertEqual(10, box.getHeight())
        self.assertEqual(100, box.getXY().getX())
        self.assertEqual(200, box.getXY().getY())
        
        box.move(xy(150, 250))
        self.assertEqual(150, box.getXY().getX())
        self.assertEqual(250, box.getXY().getY())
        
        exception1 = False
        try:
            box2 = Box("test", 5, xy(0,0))
        except BoxException:
            exception1 = True
            
        exception2 = False
        try:
            box2 = Box(4, "test", xy(0,0))
        except BoxException:
            exception2 = True
            
        exception3 = False
        try:
            box3 = Box(4, 5, "xy(0,0)")
        except BoxException:
            exception3 = True
            
        self.assertTrue(exception1)
        self.assertTrue(exception2)
        self.assertTrue(exception3)

class ArmCommandTests(unittest.TestCase):
    
    def testArmCommand(self):
        command = ArmCommand(5, 3, 75, False)
        self.assertEqual(str(command), "command: Time: 5, joint: 3, angle: 75, grab: False", "Command representation incorrect")
        
    def testGetTime(self):
        command = ArmCommand(55,17,28, True)
        self.assertEqual(command.getTime(), 55, "command returned incorrect time")
    
    def testGetJoint(self):
        command = ArmCommand(55,17,28, True)
        self.assertEqual(command.getJoint(), 17, "command returned incorrect joint")
    
    def testGetAngle(self):
        command = ArmCommand(55,17,28, False)
        self.assertEqual(command.getAngle(), 28, "command returned incorrect angle")
    
    def testGetGrabFalse(self):
        command = ArmCommand(55,17,28, False)
        self.assertFalse(command.getGrab(), "command returned grab as true")
        
    def testGetGrabTrue(self):
        command = ArmCommand(55,17,28, True)
        self.assertTrue(command.getGrab(), "command returned grab as false")  
    
class CommandCsvReaderTests(unittest.TestCase):
        
    def testCommandCsvReader(self):
        reader = CommandCsvReader()
        reader.load("../example_command_files/armCommandsForTest.csv", ';')
        commands = reader.getCommandList()
        self.assertEqual((commands[8])[1].getAngle(), 60, "Expected data not present in the commandlist")


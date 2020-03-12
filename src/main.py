from arm import Arm
from joint import Joint
from joint import Empty

def main():
    arm = Joint(5, 0, Empty())
    arm = Joint(6,30, arm)
    print(arm)
    
if __name__ == '__main__':
    main()

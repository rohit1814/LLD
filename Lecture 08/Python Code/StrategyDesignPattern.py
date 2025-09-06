# https://www.geeksforgeeks.org/python/strategy-method-python-design-patterns/

from abc import ABC, abstractmethod

class WalkableRobot(ABC):
    @abstractmethod
    def walk(self):
        pass

class NormalWalk(WalkableRobot):
    def walk(self):
        return "Walking normally."
    
class NoWalk(WalkableRobot):
    def walk(self):
        return "Cannot walk."
    
class TalkableRobot(ABC):
    @abstractmethod
    def talk(self):
        pass

class NormalTalk(TalkableRobot):
    def talk(self):
        return "Talking normally."
    
class NoTalk(TalkableRobot):
    def talk(self):
        return "Cannot talk."
    
class FlyableRobot(ABC):
    @abstractmethod
    def fly(self):
        pass

class NormalFly(FlyableRobot):
    def fly(self):
        return "Flying normally."
    
class NoFly(FlyableRobot):
    def fly(self):
        return "Cannot fly."
    
class Robot:
    def __init__(self, walk_behavior: WalkableRobot, talk_behavior: TalkableRobot, fly_behavior: FlyableRobot):
        self.walk_behavior = walk_behavior
        self.talk_behavior = talk_behavior
        self.fly_behavior = fly_behavior
        
    def walk(self):
        return self.walk_behavior.walk()
    
    def talk(self):
        return self.talk_behavior.talk()

    def fly(self):
        return self.fly_behavior.fly()
    
    @abstractmethod
    def projection(self):
        pass

class CompanionRobot(Robot):
    def projection(self):
        print("Displaying friendly companion features...")

class WorkerRobot(Robot):
    def projection(self):
        print("Displaying worker efficiency stats...")

# --- Main Function ---
if __name__ == "__main__":
    robot1 = CompanionRobot(NormalWalk(), NormalTalk(), NoFly())
    robot1.walk()
    robot1.talk()
    robot1.fly()
    robot1.projection()

    print("--------------------")

    robot2 = WorkerRobot(NoWalk(), NoTalk(), NormalFly())
    robot2.walk()
    robot2.talk()
    robot2.fly()
    robot2.projection()
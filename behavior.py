#! /bin/python

class Context:
    "状态模式的上下文环境类"
    def __init__(self):
        self.__states = []
        self.__curState = None
        self.__stateInfo = 0

    def addState(self, state):
        if(state not in self.__states):
            self.__states.append(state)

    def changeState(self, state):
        if(state is None):
            return False
        if(self.__curState is None):
            print("初始化为:", state.getStateName())
            self.__curState = state
        else:
            print("由",self.__curState.getStateName(),"变为",state.getStateName())
            self.__curState = state
            self.addState(state)
            return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if(state.isMatch(stateInfo)):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo

class State:
    "状态的基类"
    def __init__(self, name):
        self.__name = name

    def getStateName(self):
        return self.__name

    def isMatch(self, stateInfo):
        return False

    def behavior(self, context):
        pass

class Water(Context):
    def __init__(self):
        super().__init__()
        self.addState(SolidState("固态"))
        self.addState(LiquidState("液态"))
        self.addState(GaseousState("气态"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            state.behavior(self)

def singleton(cls, *args, **kwargs):
    instance = {}
    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton

@singleton
class SolidState(State):
    "固态"
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        if(isinstance(context, Water)):
            print("我性格高冷，当前体温:",context.getTemperature())

@singleton
class LiquidState(State):
    "液态"
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return (stateInfo >= 0 and stateInfo < 100)

    def behavior(self, context):
        if(isinstance(context, Water)):
            print("我性格温和，当前体温：", context.getTemperature())

@singleton
class GaseousState(State):
    "气态"
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo > 100

    def behavior(self, context):
        if(isinstance(context, Water)):
            print("我性格刚烈，当前体温：", context.getTemperature())

def testState():
    "状态模式的测试代码"
    water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()
    water.setTemperature(60)
    water.behavior()
    water.reduceTemperature(80)
    water.behavior()
if __name__ == "__main__":
       testState() 

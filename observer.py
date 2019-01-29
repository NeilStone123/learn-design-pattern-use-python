#!/usr/bin/python

class Observer:
    #"观察者基类"
    def update(self, observer, object):
        pass

class Observable:
    #"被观察者基类"
    def __init__(self):
        self.__observers = []
    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self):
        self.__observers.remove(observer)

    def notifyObservers(self, object = 0):
        for o in self.__observers:
            o.update(self, object)

class WaterHeater(Observable):
    #"热水器"
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is:", self.__temperature)
        self.notifyObservers()

class WashingMode(Observer):
    #"该模式用于洗澡"
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已经烧好，可以用来洗澡了")

class DrinkingMode(Observer):
    #"该模式用于引用"
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已经烧开，可以用来引用了")

def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)

if __name__ == "__main__":
    testWaterHeater()


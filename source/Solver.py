from source.Car import *
from source.Deffects import *
class Solver:
    def __init__(self,deffect,car,period):
        self.deffect = deffect
        self.car = car
        self.period = period
        pass
    # We will try to find probability of deffect to happen at least once
    def get_probability(self):
        return  1.0 - (1.0 - self.deffect.probability.FindProb(self.car))**self.period




    def get_diffculty(self):
        exp_val = self.period * self.deffect.probability.FindProb(self.car)
        time,cost = self.deffect.difficulty.find_diff(self.car)
        if time == -1:
            total_time = -1
            total_cost = -1
        else:
            total_time = time*exp_val
            total_cost = cost*exp_val
        return total_time,total_cost
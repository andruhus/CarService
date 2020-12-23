import datetime
now = datetime.datetime.now()
class PrCalcBase:
    def __init__(self,b,k,deffect_name):
        self.k_coef = k
        self.b_coef = b
        self.deffect_name = deffect_name
        pass

    def FindProb(self,car):
        pass
    def FindNumDeffects(self,car):
        res = 0
        for deffect in car.history_of_defects:
            if deffect[2] == self.deffect_name:
                res += 1
                pass
        return res
    def CheckRes(self,res):
        if res < 0:
            res = 0
        if res > 1:
            res = 1
        return res

class PrCalcFix(PrCalcBase):
    def FindProb(self,car):
        return self.b_coef

class PrCalcTime(PrCalcBase):
    def FindProb(self,car):
        res =  self.k_coef * (car.year - now.year) + self.b_coef
        return self.CheckRes(res)

class PrCalcUsage(PrCalcBase):
    def FindProb(self,car):
        res = self.k_coef * car.car_usage + self.b_coef
        return self.CheckRes(res)

class PrCalcHist(PrCalcBase):
    def FindProb(self,car):
        parameter = self.FindNumDeffects(car)
        res = self.k_coef * parameter + self.b_coef
        return self.CheckRes(res)
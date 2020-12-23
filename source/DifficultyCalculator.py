import datetime
now = datetime.datetime.now()

MAX_TIME_VALUE = 100
MAX_COST_VALUE = 100

manufacture_info = {
    "Audi": 0.5,
    "Mitsubishi": 0.75,
    "Folzvagen": 0.4,
    "Kia": 0.67,
    "Ford": 0.34,
    "Porsche": 0.91,
    "Lamborghini": 0.97,
    "Mersedes": 0.84
}

class DfCalcBase:
    def __init__(self,b1,b2,k1,k2,deffect_name):
        self.k_coef_time = k1
        self.b_coef_time = b1
        self.k_coef_cost = k2
        self.b_coef_cost = b2
        self.deffect_name = deffect_name
        pass

    def find_diff(self,car):
        pass

    def CheckRes(self,time,cost):
        if time > MAX_TIME_VALUE or cost > MAX_COST_VALUE:
            time = -1
            cost = -1
        return time,cost

class DfCalcFix(DfCalcBase):
    def find_diff(self,car):
        return self.b_coef_time,self.b_coef_cost

class DfCalcTime(DfCalcBase):
    def find_diff(self,car):
        res_time =  self.k_coef_time * (car.year - now.year) + self.b_coef_time
        res_cost =  self.k_coef_cost * (car.year - now.year) + self.b_coef_cost
        return self.CheckRes(res_time,res_cost)

class DfCalcUsage(DfCalcBase):
    def find_diff(self, car):
        res_time = self.k_coef_time * car.car_usage + self.b_coef_time
        res_cost = self.k_coef_cost * car.car_usage + self.b_coef_cost
        return self.CheckRes(res_time, res_cost)

class DfCalcManufacturer(DfCalcBase):
    def find_diff(self, car):
        res_time = self.k_coef_time * manufacture_info[car.manufacturer] + self.b_coef_time
        res_cost = self.k_coef_cost * manufacture_info[car.manufacturer] + self.b_coef_cost
        return self.CheckRes(res_time, res_cost)
from ProbabilityCalculator import *
from DiffcultyCalculator import *
class Deffect:
    def __init__(self,name,prob,diff):
        self.name = name
        self.probability = prob
        self.difficulty = diff
        pass

    def find_probability(self,fields):
        if fields[1] == "Fixed":
            self.probability = PrCalcFix(float(fields[2]), float(fields[3]), fields[0])
        if fields[1] == "Year":
            self.probability = PrCalcTime(float(fields[2]), float(fields[3]), fields[0])
        if fields[1] == "Car usage":
            self.probability = PrCalcUsage(float(fields[2]), float(fields[3]), fields[0])
        if fields[1] == "History":
            self.probability = PrCalcHist(float(fields[2]), float(fields[3]), fields[0])

    def find_diffculty(self,fields):
        if fields[4] == "Fixed":
            self.probability = DfCalcFix(float(fields[5]), float(fields[6]),
                                         float(fields[7]),float(fields[8]), fields[0])
        if fields[4] == "Year":
            self.probability = DfCalcTime(float(fields[5]), float(fields[6]),
                                          float(fields[7]),float(fields[8]), fields[0])
        if fields[4] == "Car usage":
            self.probability = DfCalcUsage(float(fields[5]), float(fields[6]),
                                           float(fields[7]),float(fields[8]), fields[0])
        if fields[4] == "Manufacturer":
            self.probability = DfCalcManufacturer(float(fields[5]), float(fields[6]),
                                                  float(fields[7]),float(fields[8]), fields[0])

    def __init__(self,line):
        fields = line.split(':')
        self.name = fields[0]
        self.find_probability(fields)
        self.find_diffculty(fields)
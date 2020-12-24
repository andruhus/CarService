import unittest
import sys

from source.Car import Car
from source.Deffects import Deffect
from source.Solver import Solver

sys.path.insert(1, '/Users/aaade/Desktop/programs/OOP/CarService/source')

class Main_Algorythm(unittest.TestCase):
    def test_simple(self):
        deffect = Deffect("Radiator Leak:Fixed:0.5:0.5:Fixed:0.1:0.1:0.0:0.0")
        car = Car("Mark's:Audi:2002:14")
        s = Solver(deffect,car,2)
        self.assertEqual(0.75,s.get_probability())
        self.assertEqual(s.get_diffculty(),(0.1,0.1))
    def test_year(self):
        deffect = Deffect("The Steering Wheel is Shaking:Year:0.5:0.0005:Year:0.1:0.1:0.03:0.02")
        car1 = Car("Ben's:Porsche:2002:14")
        car2 = Car("Nick's:Kia:2012:14")
        s1 = Solver(deffect, car1, 3)
        s2 = Solver(deffect, car2, 3)
        self.assertEqual(True,s1.get_probability() - s2.get_probability() > 0)

        time1,cost1 = s1.get_diffculty()
        time2,cost2 = s2.get_diffculty()
        self.assertEqual(True,time1 - time2 > 0)
        self.assertEqual(True,cost1 - cost2 > 0)
    def test_usage(self):
        deffect = Deffect("The Engine is Sputtering:Car usage:0.5:0.0005:Car usage:0.1:0.1:0.03:0.02")
        car1 = Car("Ben's:Porsche:2002:14")
        car2 = Car("Nick's:Kia:2012:28")
        s1 = Solver(deffect, car1, 3)
        s2 = Solver(deffect, car2, 3)
        self.assertEqual(True,s1.get_probability() - s2.get_probability() < 0)

        time1, cost1 = s1.get_diffculty()
        time2, cost2 = s2.get_diffculty()
        self.assertEqual(True, time1 - time2 < 0)
        self.assertEqual(True, cost1 - cost2 < 0)
    def test_manufacturer_n_history(self):
        deffect = Deffect("The Brake Pads are Worn:History:0.5:0.0005:Manufacturer:0.1:0.1:0.03:0.02")
        car1 = Car("Ben's:Porsche:2002:14")
        car2 = Car("Nick's:Kia:2012:28")
        s1 = Solver(deffect, car1, 3)
        s2 = Solver(deffect, car2, 3)
        self.assertEqual(s1.get_probability() , s2.get_probability())
        time1, cost1 = s1.get_diffculty()
        time2, cost2 = s2.get_diffculty()
        self.assertEqual(True, time1 - time2 > 0)
        self.assertEqual(True, cost1 - cost2 > 0)
if __name__ == '__main__':
    unittest.main()

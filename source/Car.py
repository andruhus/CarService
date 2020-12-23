
class Car:
    def __init__(self,name,manufacturer,year,car_usage,history_of_defects):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.car_usage = car_usage
        self.history_of_defects = history_of_defects
        pass
    def __init__(self,line):
        fields = line.split(':')
        self.name = fields[0]
        self.manufacturer = fields[1]
        self.year = int(fields[2])
        self.car_usage = int(fields[3])
        self.history_of_defects = []
        temp = fields[4].split(';')
        for item in temp:
            self.history_of_defects.append(item.split())
    def get_string(self):
        str = self.name + ":" + self.manufacturer + ":"
        str += str(self.year) + ":" + str(self.car_usage) + ":"
        for item in self.history_of_defects:
            str += item[0] + " " + item[1] + " " + item[2] + ";"
        return str

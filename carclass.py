class car:
    def __init__(self,year,make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def returnspeed(self):
        return self.__speed

    def acceleration(self):
        currentspeed = self.__speed
        newspeed = currentspeed + 5
        self.__speed = newspeed
        
    def brake(self):
        brakespeed = self.__speed
        newbrakespeed = brakespeed - 5
        self.__speed = newbrakespeed

    def set_year(self,year):
        self.__year = year

    def set_make(self,make):
        self.__make = make

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make
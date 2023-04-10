#lex_auth_0127426245709905921377

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))
    
    # Write Service Class as given in class diagram that performs various activities on a list of cars
    # Implement Service class here

class Service:
    def __init__(self, car_list):
        self.__car_list = car_list
        
    def get_car_list(self):
        self.__car_list    
        
    def find_cars_by_year (self, year):
        list1 = []
        for car in self.__car_list:
            if int(car.get_year()) == year:
                list1.append(car.get_model())
        if len(list1) == 0:
            return None
        return list1
    
    def add_cars (self, new_car_list):
        self.__car_list.extend(new_car_list)
        self.__car_list.sort(key = lambda x: x.get_year())
    
    def remove_cars_from_karnataka (self):
        list1 = self.__car_list.copy()
        for car in list1:
            if car.get_registration_number()[0:2] == "KA":
                self.__car_list.remove(car)
    
car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program
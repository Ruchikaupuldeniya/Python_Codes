class Car:
    def __init__(self,brand,model,year):

        self.brand = brand
        self.model = model
        self.year = year

    def displayCarInfo(self):
        print(f"Car Brand:{self.brand},medel:{self.model},year:{self.year}")

car1=Car("Toyota","Civic",2024)
car2=Car("BMW","XI",2024)
car3=Car("BMW","MI",2024)

car1.displayCarInfo(),car2.displayCarInfo()

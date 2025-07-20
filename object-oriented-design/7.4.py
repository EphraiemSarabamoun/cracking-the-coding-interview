class ParkingLot:
    def __init__(self):
        self.spaces = []
    def handle_car_parking(self,car):
        for space in self.spaces:
            if space.occupied == False:
                space.car_parking(car)
                return     
        print("Parking lot is full")
        return
    def handle_car_leaving(self,car):
        for space in self.spaces:
            if space.car_id == car.id:
                space.car_leaving()
                return
        print("No car parked")
        return

class ParkingSpace:
    def __init__(self, spot):
        self.occupied = False
        self.car_id = None
    def car_parking(self,car):
        self.occupied = True
        self.car_id = car.id
    def car_leaving(self):
        self.occupied = False
        self.car_id = None
class Car:
    def __init__(self, id):
        self.id = id

if __name__ == "__main__":
    cars = [Car(i) for i in range(11)]
    parkinglot = ParkingLot()
    parkinglot.spaces = [ParkingSpace(i) for i in range(10)]   
    for car in cars:
        parkinglot.handle_car_parking(car)
    for i in range(0,11):
        parkinglot.handle_car_leaving(cars[i])

class Parent:
    def __init__(self, lands, houses, cars):
        self.lands = lands
        self.houses = houses
        self.cars = cars

    def total_parent_assets(self):
        print("Parent Land", self.lands, "acres")
        print("Parent Houses", self.houses)
        print("Parent cars", self.cars)

class Child(Parent):
    def __init__(self, lands, houses, cars, bike):
        super().__init__(lands, houses, cars)
    
        self.bike = bike

    def total_child_assets(self):
        self.total_parent_assets()
        print("Child total vehicles", self.cars + self.bike)


obj = Child(2, 3, 3, 2)
obj.total_child_assets()

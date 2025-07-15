class BankLocker:
    def __init__(self):
        self.documents = "land Propety docs"
        self.__gold_quantity = "20 grams"

    def modify_properties(self, gold_quantity):
        self.__gold_quantity = gold_quantity

    def current_items_in_locker(self):
        print(f"{self.documents}")
        print(f"{self.__gold_quantity}")
    

obj = BankLocker()
obj.documents = "car documents"
obj.current_items_in_locker()





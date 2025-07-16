class CarCatalog:
  def __init__(self, brand, model, exterior_color, interior_color, price):
    self.brand = brand
    self.model = model
    self.exterior_color = exterior_color
    self.interior_color = interior_color
    self.price = price
  def show_selected_car__details(self, name):
      print("----------------------------")
      print(f"{name} Selected Car Details")
      print(f"Car Brand: {self.brand}")
      print(f"Car Brand: {self.model}")
      print(f"Car Brand: {self.exterior_color}")
      print(f"Car Brand: {self.interior_color}")
      print(f"Car Brand: {self.price}")
      print("----------------------------")

# Only runs when this file is executed directly
  karthik_car_details = CarCatalog("Honda", "City", "red", "beige", "25000000")
  arjun_car_details = CarCatalog("BMW", "X3", "black", "beige", "50000000")
  
  karthik_car_details.show_selected_car__details('Karthik')
  arjun_car_details.show_selected_car__details('Arjun')

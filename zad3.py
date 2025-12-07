class Property:
  def __init__(self, area, rooms, price, address):
    self.area = area
    self.rooms = rooms
    self.price = price
    self.address = address

class House(Property):
  def __init__(self, area, rooms, price, address, plot):
    super().__init__(area, rooms, price, address)
    self.plot = plot

  def __str__(self):
    return (f"Dom o powierzchni: {self.area} m², ilość pokoi: {self.rooms}, cena: {self.price} zł, adres: {self.address}, rozmiar działki: {self.plot} m²")

class Flat(Property):
  def __init__(self, area, rooms, price, address, floor):
    super().__init__(area, rooms, price, address)
    self.floor = floor

  def __str__(self):
    return (f"Mieszkanie o powierzchni: {self.area} m², Ilość pokoi: {self.rooms}, cena: {self.price} zł, adres: {self.address}, piętro: {self.floor}")
  

house = House(150, 6, 1200000, "Katowice, ul. Kanałowa 2", 320)
flat = Flat(33, 2, 500000, "Katowice, ul. Mikołowska 124/9", 3)

print(house)
print(flat)
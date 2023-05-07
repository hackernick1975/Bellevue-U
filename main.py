make=input(f"What is the make of the vehicle?\n")
model=input(f"What is the model of the vehicle?\n")
vehicle_choice=input("Is the vehicle a car or truck?\n")


class Vehicle:
  def __init__(self, make, model):
   self.make=make
   self.model=model

if vehicle_choice=="car":
  doors=input(f"How many doors does the car have?\n")
  class Car(Vehicle):
    def __init__(self, doors):
      self.doors=doors
    print(f"Your {make} {model} has {doors} doors on it.")
elif vehicle_choice=="truck":
  length=input(f"What is the length of the bed?\n")
  class Truck(Vehicle):
    def __init__(self, length):
      self.length=length
    print(f"Your {make} {model} has a {length} foot bed.")

else:
  print("Invalid input, please enter 'car' or 'truck'.")





from car import Car


model = input("enter the model: ")


while (True):
    try:
        year = input("enter the year: ")
        if int(year) > 2020 or int(year) < 1945:
            year = input("Invalid year. Try again. Enter the car's year model: ")
        if (int(year) > 1945 and int(year) <2020):
            break
    except ValueError:
        year = input("Invalid input: a numeric value was expected. Try again. Enter the car's year model:")

car1 = Car(model,year)
print()
print("My car's make: " + str(car1.getMake()))
print("My car's year: " + str(car1.getYear()))
print("My car's current speed: "+ str(car1.getSpeed())+" mph.")
print()
print("Accelerating")
while car1.getSpeed() < 50:
    car1.accelerate()
    print("My car's current speed: " + str(car1.getSpeed()) +".")
print()
print("Slowing down")
while car1.getSpeed() >0:
    car1.brake()
    print("My car's current speed: " + str(car1.getSpeed()) +".")
    
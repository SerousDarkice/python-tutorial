cars = 100 # assign cars the integer 100
space_in_a_car = 4.0 # assign space_in_a_car the floating point number 4
drivers = 30 # assign drivers the integer 30
passengers = 90 # assign passengers the integer 90
cars_not_driven = cars - drivers # assign cars_not_drive the difference between cars and drivers
cars_driven = drivers # assign the value of cars_driven the value of drivers
carpool_capacity = cars_driven * space_in_a_car # assing carpool_capacity the value of of the product of cars_driven and space_in_a_car
average_passengers_per_car = passengers / cars_driven # assign average_passengers_per_car the quotient of passengers and cars_driven


print("There are", cars, "cars available.") # print strings and the value of cars
print("There are only", drivers, "drivers avialable") # print strings and the value of drivers
print("There will be", cars_not_driven, "empty cars today.") # print strings and the value of cars_not_driven
print("We can transport", carpool_capacity, "people today.") # print strings and the value of carpool_capacity
print("We have", passengers, "to carpool today.") # print strings and the value of passengers
print("We need to put about", average_passengers_per_car, # print string and the value of average_passengers_per_car
      "in each car.") # print string

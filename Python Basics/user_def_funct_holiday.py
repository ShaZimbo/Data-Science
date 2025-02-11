""" This program calculates the cost of a holiday based on user input. """


def city_options():
    """ Print the city destinations available to the user. """
    print("City destinations:")
    print("z = Zimbabwe")
    print("c = Crete")
    print("m = Manchester")
    print("p = Paris")
    print("e = Exit")


def plane_cost(dest):
    """ Return the cost of the flight to the selected destination. """
    plane_prices = {"z": 750, "c": 325, "m": 100, "p": 250}
    return plane_prices.get(dest, "Destination not found.")


def city_destination(city):
    """ Return the full name of the city destination. """
    destinations = {
        "z": "Zimbabwe",
        "c": "Crete",
        "m": "Manchester",
        "p": "Paris"}
    return destinations.get(city, "Unknown destination")


def hotel_cost(num_nights):
    """ Return the cost of the hotel stay. """
    price = num_nights * 550
    return price


def car_rental(rental_days):
    """ Return the cost of the car rental. """
    rental_cost = rental_days * 125
    return rental_cost


def holiday_cost(f, h, c):
    """ Return the total cost of the holiday. """
    holiday_price = f + h + c
    return holiday_price


# Calculate costs based on user selection
print("This programme will calculate the cost of your holiday:")
DESTINATION = ""
city_options()

while DESTINATION != "e":
    DESTINATION = input("Please enter your destination: ").lower()
    if DESTINATION in ["z", "c", "m", "p"]:
        plane_cost(DESTINATION)
        city_destination(DESTINATION)
        break
    elif DESTINATION == "e":
        print("You have exited")
        exit()
    else:
        print("That destination is not recognised")

nights = int(input
             ("Please enter the number of nights you will stay in the hotel: ")
             )
hotel_cost(num_nights=nights)

days = int(input
           ("Please enter the number of days you will be renting a car: ")
           )
car_rental(rental_days=days)

plane_price = plane_cost(DESTINATION)
hotel_price = hotel_cost(nights)
car_price = car_rental(days)

# Add to get the total cost of the holiday
print(f"\nYour travel arrangements and costs:\n"
      f"You will be travelling to {city_destination(DESTINATION)}.\n"
      f"Flight costs: £{plane_price}\n"
      f"Hotel stay for {nights} nights will cost: £{hotel_price}\n"
      f"Car rental for {days} days will cost: £{car_price}\n"
      f"This holiday will cost a total of: £"
      f"{holiday_cost(plane_price, hotel_price, car_price)}"
      )

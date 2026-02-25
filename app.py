# app.py

def calculate_fare(distance_km):
    base_fare = 50          # base fare in rupees
    per_km_rate = 15        # cost per km
    return base_fare + (distance_km * per_km_rate)


def main():
    print("===================================")
    print("     SIMPLE TAXI BOOKING SYSTEM     ")
    print("===================================")

    name = input("Enter customer name: ")
    pickup = input("Enter pickup location: ")
    drop = input("Enter drop location: ")
    distance = float(input("Enter distance (in km): "))

    fare = calculate_fare(distance)

    print("\n--------- BOOKING CONFIRMATION ---------")
    print(f"Customer Name : {name}")
    print(f"Pickup Point  : {pickup}")
    print(f"Drop Point    : {drop}")
    print(f"Distance      : {distance} km")
    print(f"Total Fare    : ₹{fare}")
    print("----------------------------------------")
    print("Taxi booked successfully 🚕")
    print("Thank you for using our service!")


if __name__ == "__main__":
    main()

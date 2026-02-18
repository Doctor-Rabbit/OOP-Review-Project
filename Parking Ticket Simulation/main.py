"""
Interactive main program for the Parking Ticket System.
Prompts the user for input instead of using fixed scenarios.
"""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def get_positive_int(prompt: str) -> int:
    """Prompt until the user enters a valid positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")


def get_car_from_user() -> ParkedCar:
    """Collect car information from the user."""
    print("\nEnter parked car information:")
    make = input("Make: ")
    model = input("Model: ")
    color = input("Color: ")
    license_number = input("License number: ")
    minutes_parked = get_positive_int("Minutes parked: ")

    return ParkedCar(make, model, color, license_number, minutes_parked)


def get_meter_from_user() -> ParkingMeter:
    """Collect parking meter information from the user."""
    minutes_purchased = get_positive_int("Minutes purchased on meter: ")
    return ParkingMeter(minutes_purchased)


def main() -> None:
    print("=== Parking Ticket System ===")

    # Officer info (entered once)
    print("\nEnter police officer information:")
    officer_name = input("Officer name: ")
    badge_number = input("Badge number: ")
    officer = PoliceOfficer(officer_name, badge_number)

    while True:
        car = get_car_from_user()
        meter = get_meter_from_user()

        ticket = officer.inspect_car(car, meter)

        if ticket is None:
            print("\nRESULT: The car is legally parked. No ticket issued.")
        else:
            print("\nRESULT:")
            print(ticket)

        again = input("\nInspect another car? (y/n): ").lower()
        if again != "y":
            print("\nExiting Parking Ticket System.")
            break


if __name__ == "__main__":
    main()

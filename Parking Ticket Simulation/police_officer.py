"""
PoliceOfficer class for the Parking Ticket System simulation.

Inspects a car and meter; if illegally parked, returns a ParkingTicket, else None.
"""
from __future__ import annotations

from typing import Optional

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Simulates a police officer inspecting parked cars."""

    def __init__(self, name: str, badge_number: str) -> None:
        self.name = str(name)
        self.badge_number = str(badge_number)

    def inspect_car(self, car: ParkedCar, meter: ParkingMeter) -> Optional[ParkingTicket]:
        """
        Determine whether the car is illegally parked.

        Returns:
            ParkingTicket if minutes_parked > minutes_purchased, else None.
        """
        if car.minutes_parked > meter.minutes_purchased:
            illegal_minutes = car.minutes_parked - meter.minutes_purchased
            return ParkingTicket(car=car, officer=self, illegal_minutes=illegal_minutes)
        return None

    def __str__(self) -> str:
        return f"Officer: {self.name} (Badge {self.badge_number})"

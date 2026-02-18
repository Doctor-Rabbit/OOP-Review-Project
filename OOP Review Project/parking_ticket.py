"""
ParkingTicket class for the Parking Ticket System simulation.

Fine rule:
- $25 for the first hour or part of an hour
- +$10 for each additional hour or part of an hour
"""
from __future__ import annotations

import math

from parked_car import ParkedCar


class ParkingTicket:
    """Represents a citation issued for a car parked beyond the paid time."""

    def __init__(self, car: ParkedCar, officer, illegal_minutes: int) -> None:
        self.car = car  # retains reference to the ParkedCar object (composition)
        self.officer_name = str(officer.name)
        self.badge_number = str(officer.badge_number)

        if not isinstance(illegal_minutes, int):
            raise TypeError("illegal_minutes must be an integer.")
        if illegal_minutes <= 0:
            raise ValueError("illegal_minutes must be a positive integer (> 0).")
        self.illegal_minutes = illegal_minutes

        self.fine = self.calculate_fine()

    def calculate_fine(self) -> float:
        """
        Calculate fine based on illegal minutes.

        $25 for first hour (or part) + $10 for each additional hour (or part)
        """
        hours = int(math.ceil(self.illegal_minutes / 60))
        if hours <= 1:
            return 25.0
        return 25.0 + (hours - 1) * 10.0

    def __str__(self) -> str:
        return (
            "==== Parking Ticket ====\n"
            f"{self.car}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:,.2f}\n"
            f"Issued By: {self.officer_name} (Badge {self.badge_number})\n"
            "========================"
        )

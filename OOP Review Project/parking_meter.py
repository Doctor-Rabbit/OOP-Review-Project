"""
ParkingMeter class for the Parking Ticket System simulation.

minutes_purchased is private with property validation.
"""
from __future__ import annotations


class ParkingMeter:
    """Simulates a parking meter."""

    def __init__(self, minutes_purchased: int = 60) -> None:
        self._minutes_purchased: int = 60
        self.minutes_purchased = minutes_purchased  # validates

    @property
    def minutes_purchased(self) -> int:
        """Minutes purchased on the meter (must be > 0)."""
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("minutes_purchased must be an integer.")
        if value <= 0:
            raise ValueError("minutes_purchased must be a positive integer (> 0).")
        self._minutes_purchased = value

    def __str__(self) -> str:
        return f"ParkingMeter: Minutes Purchased = {self.minutes_purchased}"

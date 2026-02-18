"""
ParkedCar class for the Parking Ticket System simulation.

See assignment specs: minutes_parked must be private with property validation.
"""
from __future__ import annotations


class ParkedCar:
    """Simulates a parked car."""

    def __init__(
        self,
        make: str,
        model: str,
        color: str,
        license_number: str,
        minutes_parked: int = 60,
    ) -> None:
        self.make = str(make)
        self.model = str(model)
        self.color = str(color)
        self.license_number = str(license_number)
        self._minutes_parked: int = 60  # set default first
        self.minutes_parked = minutes_parked  # validates

    @property
    def minutes_parked(self) -> int:
        """Minutes the car has been parked (must be > 0)."""
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("minutes_parked must be an integer.")
        if value <= 0:
            raise ValueError("minutes_parked must be a positive integer (> 0).")
        self._minutes_parked = value

    def __str__(self) -> str:
        return (
            f"Car: {self.make} {self.model} | Color: {self.color} | "
            f"License: {self.license_number} | Minutes Parked: {self.minutes_parked}"
        )

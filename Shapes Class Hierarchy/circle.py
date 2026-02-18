from __future__ import annotations
import math
from basic_shape import BasicShape

class Circle(BasicShape):
    """Circle shape (area = pi * r^2)."""

    def __init__(self, x: float, y: float, r: float, n: str = "Circle") -> None:
        super().__init__(n)
        self._x_center: float = float(x)
        self._y_center: float = float(y)
        self._radius: float = 1.0
        self.radius = r  # validates + recalculates area

    def calc_area(self) -> None:
        self._area = math.pi * (self._radius ** 2)

    @property
    def x_center(self) -> float:
        return self._x_center

    @property
    def y_center(self) -> float:
        return self._y_center

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("radius must be > 0")
        self._radius = value
        self.calc_area()

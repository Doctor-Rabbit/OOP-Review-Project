from __future__ import annotations
from basic_shape import BasicShape

class Rectangle(BasicShape):
    """Rectangle shape (area = length * width)."""

    def __init__(self, l: float, w: float, n: str = "Rectangle") -> None:
        super().__init__(n)
        self._length: float = 1.0
        self._width: float = 1.0
        self.length = l
        self.width = w

    def calc_area(self) -> None:
        self._area = self._length * self._width

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("length must be > 0")
        self._length = value
        self.calc_area()

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value
        self.calc_area()

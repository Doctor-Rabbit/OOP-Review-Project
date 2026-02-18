from __future__ import annotations
from rectangle import Rectangle

class Square(Rectangle):
    """Square (inherits Rectangle's calc_area)."""

    def __init__(self, s: float, n: str = "Square") -> None:
        self._side: float = 1.0
        self.side = s  # validate
        super().__init__(self._side, self._side, n)
        self.name = n  # ensure BasicShape name is set

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, value: float) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("side must be > 0")
        self._side = value
        if hasattr(self, "_length") and hasattr(self, "_width"):
            self._length = value
            self._width = value
            self.calc_area()

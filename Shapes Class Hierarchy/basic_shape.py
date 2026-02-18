from __future__ import annotations
from abc import ABC, abstractmethod

class BasicShape(ABC):
    """Abstract base class for geometric shapes."""

    def __init__(self, name: str = "BasicShape") -> None:
        self._area: float = 0.0
        self._name: str = str(name)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = str(value)

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, value: float) -> None:
        self._area = float(value)

    @abstractmethod
    def calc_area(self) -> None:
        """Compute and store the shape's area in self._area."""
        raise NotImplementedError

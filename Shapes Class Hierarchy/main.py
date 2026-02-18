from __future__ import annotations
from circle import Circle
from rectangle import Rectangle
from square import Square

def fmt_area(a: float) -> str:
    if abs(a - round(a)) < 1e-9:
        return str(int(round(a)))
    return f"{a:.5f}"

def main() -> None:
    shapes = [
        Circle(0, 0, 4, "Circle_1"),
        Circle(1, 2, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(20, 30, "Rectangle_2"),
        Square(10, "Square"),
    ]

    print("--- Polymorphism check ---")
    for s in shapes:
        print(f"{s.name} Area = {fmt_area(s.area)}")

    print("--- Getter/setter check ---")

    c = shapes[0]
    print(f"{c.name} Current: {c.radius:g} {fmt_area(c.area)}")
    c.radius = c.radius * 2
    print(f"{c.name} Doubled: {c.radius:g} {fmt_area(c.area)}")

    r = shapes[2]
    print(f"{r.name} Current: {r.length:g} {r.width:g} {fmt_area(r.area)}")
    r.length = r.length * 2
    r.width = r.width * 2
    print(f"{r.name} Doubled: {r.length:g} {r.width:g} {fmt_area(r.area)}")

    sq = shapes[4]
    print(f"{sq.name} Current: {sq.side:g} {fmt_area(sq.area)}")
    sq.side = sq.side * 2
    print(f"{sq.name} Doubled: {sq.side:g} {fmt_area(sq.area)}")

if __name__ == "__main__":
    main()

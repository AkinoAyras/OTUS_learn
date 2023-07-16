import pytest

from hw2.src.rectangle import *
from hw2.src.circle import *

def test_rectangle():
    r = Rectangle(1, 2)
    assert r.name == 'rectangle'
    assert r.get_area() == 2
    assert r.get_perimeter() == 6

@pytest.mark.parametrize('side_a, side_b, perimetr, area',[
                            (-1, 2, 2, -2),
                            (0, 10, 20, 0)
                        ])
def test_rectangle_negative(side_a, side_b, perimetr, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_circle():
    c = Circle(5)
    assert c.name == 'circle'
    assert c.get_area() == 78
    assert c.get_perimeter() == 31

@pytest.mark.parametrize('radius, perimetr, area',[
                            (-1, -6, 3),
                            ])
def test_circle_negative(radius, perimetr, area):
    with pytest.raises(ValueError):
        Rectangle(radius)


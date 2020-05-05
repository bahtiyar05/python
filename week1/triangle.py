import math
def area(base,height):
    '''(number) -> number

    Return the  area of a triangle with given base and
    >>>area(10, 40)
    200.0
    >>>area(3.4, 7.5)
    12.75
    '''
    return base* height / 2


def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return  the perimeter of the triangle with sides of
    lenght side1, side2, side3.

    >>>perimeter(3, 4, 5)
    12
    >>>perimeter(10.5, 6, 9.3)
    25.8
    '''
    return side1+side2+side3

def semiperimeter(side1,side2,side3):
    '''(number, number, number) -> float
    Return the semiperimeter of a triangle with sides of
    leght side1, side2,side3.


    '''
    return perimeter(side1,side2,side3)/2


def area_hero(side1,side2,side3):
    ''' (Number, number,number) -> float
    >>> area_hero(3,4,5)
    6.0
    >>> area_hero(10.5,6,9.30)
    27.731
    '''
    semi = semiperimeter(side1,side2,side3)
    area = math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
    return area



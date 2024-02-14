import math

def calc_area_square(side_length: float) -> float:
    area = side_length ** 2
    return area

def calc_area_rectangle(side_length_1, side_length_2):
    if side_length_1 == side_length_2:
        return side_length_1**2
    else:
        return side_length_1 * side_length_2
input_number = 2
output_number = calc_area_square(input_number)
print(f'calc_area_square({input_number}) = {output_number}')

def calc_area_circle(radii):
    if not isinstance(radii, (float,int)):
        raise TypeError(f"radius is {radii} but must be a number")
    if radii < 0:
        raise ValueError("The radius cannot be negative")
    areas = math.pi * radii**2
    return areas

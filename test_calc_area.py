from pytest import approx, raises

def test_calc_area_square():
    from calc_area import calc_area_square

    input_number = [0, 1, 4, 100]
    output_number = [0, 1, 16, 10000]
    assert len(input_number) == len(output_number)

    for input, output in zip(input_number, output_number):
        assert calc_area_square(input) == output

def test_calc_area_rectangle():
    from calc_area import calc_area_rectangle

    assert calc_area_rectangle(2, 2) == 4
    assert calc_area_rectangle(2,1) == 2
    
def test_calc_area_circle():
    from calc_area import calc_area_circle

    assert (calc_area_circle(2)) == approx(12.5663, abs = 1e-3)

def test_calc_area_circle_errors():
    from calc_area import calc_area_circle

    with raises(ValueError):
        calc_area_circle(-1.0)
    
    with raises(TypeError):
        calc_area_circle("this is not a number")

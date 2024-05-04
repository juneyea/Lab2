import Lab2 as test

def test_find_min_max():
    y =  [2,19,3,5,-10]
    result = test.find_min_max(y)
    assert result == [19.0,-10.0]

def test_calc_average():
    y = [2,4,6,8]
    result = test.calc_average(y)
    assert result == 5.0

def test_calc_median_temperature():
    y= [2,4,6,8,10]
    result = test.calc_median_temperature(y)   
    assert result == 6

def test_calc_median_temperature_odd():
    y= [2,4,6,8,10,12]
    result = test.calc_median_temperature(y)   
    assert result == 7
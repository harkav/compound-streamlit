from utils.compound_interest import calculate_compound

def test_calculate_compound(): 
    
    assert calculate_compound(1000, 10, 1) == 1100
    assert calculate_compound(2000, 5, 1) == 2100
    assert round(calculate_compound(1000, 10, 10), 4) == 2593.7425
    assert round(calculate_compound(1_000_000, 8, 15), 4) == 3172169.1142
    assert round(calculate_compound(0, 10, 100)) == 0
    assert calculate_compound(1000, 0, 10) == 1000
    assert calculate_compound(1000, 10, 0) == 1000
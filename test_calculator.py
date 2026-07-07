import calculator

def test_addition():
    # Push the button and check if 2 + 2 equals 4
    result = calculator.add_numbers(2, 2)
    assert result == 4
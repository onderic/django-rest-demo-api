from myapp.views import add_numbers


def test_add_numbers():
    """Test for the add_numbers() function."""
    # Test case 1: Positive numbers
    assert add_numbers(2, 3) == 5
    
    # Test case 2: Negative numbers
    assert add_numbers(-2, -3) == -5
    
    # Test case 3: Zeroes
    assert add_numbers(0, 0) == 0
    
    # Test case 4: Mixed positive and negative numbers
    assert add_numbers(5, -3) == 2
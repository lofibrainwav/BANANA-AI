"""
Basic test examples for BANANA-AI
"""
import pytest

def test_import():
    """Test that we can import the main package"""
    try:
        import banana_ai
        assert True
    except ImportError:
        pytest.fail("Failed to import banana_ai")

def test_basic_math():
    """A simple test to demonstrate pytest"""
    assert 1 + 1 == 2
    assert 2 * 2 == 4

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
])
def test_square(input, expected):
    """Test with multiple inputs using parametrize"""
    assert input * input == expected 
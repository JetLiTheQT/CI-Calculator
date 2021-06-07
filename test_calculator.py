"""
Test for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3,2)
    
    def test_difference(self):
        assert 5 == calculator.difference(10,5)
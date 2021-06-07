"""
Test for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)   

    def test_difference(self):
        assert 5 == calculator.difference(10, 5)
     
    def test_multiple(self):
        assert 4 == calculator.multiply(2, 2)

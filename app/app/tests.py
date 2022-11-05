"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(3, 5)

        self.assertEqual(res, 8)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(5, 3)

        self.assertEqual(res, 2)

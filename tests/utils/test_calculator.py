from tests.set_up import BaseTest
from utils.calc import calculator


class TestCalculator(BaseTest):
    def test_calculator(self):
        res = calculator(2, 90)
        self.assertEqual(92, res)

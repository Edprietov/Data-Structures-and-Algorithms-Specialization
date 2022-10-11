from Week_2.fibonnacci import calculate_fibonnacci
import unittest


class TestCalculateFibonnacci(unittest.TestCase):
    def test_fibonnacci_0(self):
            self.assertEqual(calculate_fibonnacci(0), 0)

    def test_fibonnacci_1(self):
        self.assertEqual(calculate_fibonnacci(1), 1)

    def test_fibonnacci_2(self):
        self.assertEqual(calculate_fibonnacci(2), 1)

if __name__ == '__main__':
    unittest.main()

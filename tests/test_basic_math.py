import unittest


class TestBasicMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_multiplication(self):
        self.assertEqual(4 * 3, 12)


if __name__ == "__main__":
    unittest.main()

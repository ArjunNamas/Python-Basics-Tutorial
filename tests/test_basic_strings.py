import unittest


class TestBasicStrings(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual("python".upper(), "PYTHON")

    def test_word_length(self):
        self.assertEqual(len("code"), 4)


if __name__ == "__main__":
    unittest.main()

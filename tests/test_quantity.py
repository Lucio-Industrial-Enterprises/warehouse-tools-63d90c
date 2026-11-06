import unittest

from warehouse.quantity import parse_quantity


class QuantityParserTests(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_whitespace_trimmed(self):
        self.assertEqual(parse_quantity("  10  "), 10)

    def test_zero(self):
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")

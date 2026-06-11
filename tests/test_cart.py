import unittest

from github_demo.cart import CartItem, cart_total
from github_demo.demo_app import build_sample_cart, format_cart


class CartTests(unittest.TestCase):
    def test_item_subtotal(self):
        item = CartItem("Coffee", 2, 4.5)

        self.assertEqual(item.subtotal(), 9.0)

    def test_cart_total(self):
        items = [
            CartItem("Coffee", 2, 4.5),
            CartItem("Notebook", 1, 7.25),
        ]

        self.assertEqual(cart_total(items), 16.25)

    def test_rejects_negative_quantity(self):
        item = CartItem("Coffee", -1, 4.5)

        with self.assertRaises(ValueError):
            item.subtotal()

    def test_demo_app_formats_sample_cart(self):
        output = format_cart(build_sample_cart())

        self.assertIn("Demo Cart", output)
        self.assertIn("Coffee: 2 x $4.50 = $9.00", output)
        self.assertIn("Total: $19.85", output)


if __name__ == "__main__":
    unittest.main()

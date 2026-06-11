import unittest

from github_demo.cart import CartItem, cart_total


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


if __name__ == "__main__":
    unittest.main()

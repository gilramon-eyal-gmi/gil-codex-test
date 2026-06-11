from dataclasses import dataclass


@dataclass(frozen=True)
class CartItem:
    name: str
    quantity: int
    unit_price: float

    def subtotal(self) -> float:
        if self.quantity < 0:
            raise ValueError("quantity cannot be negative")
        if self.unit_price < 0:
            raise ValueError("unit_price cannot be negative")
        return round(self.quantity * self.unit_price, 2)


def cart_total(items: list[CartItem]) -> float:
    return round(sum(item.subtotal() for item in items), 2)

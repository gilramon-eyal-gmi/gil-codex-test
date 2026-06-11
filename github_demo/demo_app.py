from github_demo.cart import CartItem, cart_total


def build_sample_cart() -> list[CartItem]:
    return [
        CartItem("Coffee", 2, 4.50),
        CartItem("Notebook", 1, 7.25),
        CartItem("Pen", 3, 1.20),
    ]


def format_cart(items: list[CartItem]) -> str:
    lines = ["Demo Cart", "---------"]
    for item in items:
        lines.append(
            f"{item.name}: {item.quantity} x ${item.unit_price:.2f} = ${item.subtotal():.2f}"
        )
    lines.append("---------")
    lines.append(f"Total: ${cart_total(items):.2f}")
    return "\n".join(lines)


def main() -> None:
    print(format_cart(build_sample_cart()))


if __name__ == "__main__":
    main()

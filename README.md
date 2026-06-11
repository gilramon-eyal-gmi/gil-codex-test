# GitHub Demo Project

A tiny Python project for practicing the GitHub workflow with Codex.

The app calculates simple totals for a shopping cart. It is intentionally small
so commits, diffs, tests, and pull requests are easy to inspect.

## Run Tests

```powershell
python -m unittest discover -s tests
```

## Run Demo App

```powershell
python -m github_demo.demo_app
```

## Example

```python
from github_demo.cart import CartItem, cart_total

items = [
    CartItem("Coffee", 2, 4.50),
    CartItem("Notebook", 1, 7.25),
]

print(cart_total(items))
```

## GitHub Workflow To Try

1. Make or ask Codex to make a small change.
2. Run the tests.
3. Commit the change.
4. Push a branch to GitHub.
5. Open a pull request.

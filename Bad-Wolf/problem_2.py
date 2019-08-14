

def max_product(n: list, k: int)->int:
    """Намира най-голямото произведенение на sublist на n с дължина k."""
    product = 1
    for num in sorted(n, reverse=True)[:k]:
        product = product * num
    return product

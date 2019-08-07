

def divisible_by_d(n: list, d: int)->list:
    """Намира всички числа от n, които са делят на d без остатък."""
    return [i for i in n if i % d == 0]

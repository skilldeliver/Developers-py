

def divisible_by_d(n: list, d: int)->list:
    """Намира всички числа от n, които са делят на d без остатък."""
    return [num for num in n if num % d == 0]

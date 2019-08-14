from functools import reduce
from math import gcd


def convert_fracts(q: list)->list:
    """Намира дробите след привеждане под общ знаменател."""
    if not q:
        return []
    common = reduce(lambda a, b: a * b // gcd(a, b), [num[1] for num in q])
    return [[common * x[0] // x[1], common] for x in q]

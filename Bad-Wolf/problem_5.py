from itertools import permutations


def middle_permutation(s: str)->str:
    """Намира средната пермутация на s."""
    permutations_list = sorted([''.join(x) for x in list(permutations(s))], reverse=True)
    return permutations_list[len(permutations_list)//2]

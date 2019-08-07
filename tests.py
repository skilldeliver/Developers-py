from functools import partial
from timeit import Timer
from time import time, sleep

from problem_1 import divisible_by_d
from problem_2 import max_product
from problem_3 import b
from problem_4 import convert_fracts
from problem_5 import middle_permutation



def test_problem_1():
    from random import random
    from math import floor

    fixed_tests = {
    'Тест 1: ': 
        {
            'ans': divisible_by_d([1,2,3,4,5,6], 2),
            'exc': [2,4,6]
        },
    'Тест 2: ':
        {
            'ans': divisible_by_d([1,2,3,4,5,6], 3),
            'exc': [3,6]
        },
    'Тест 3: ':
        {
            'ans': divisible_by_d([0,1,2,3,4,5,6], 4),
            'exc': [0,4]
        },
    'Тест 4: ':
        {
            'ans': divisible_by_d([0], 4),
            'exc': [0]
        },
    'Тест 5: ':
        {
            'ans': divisible_by_d([1,3,5], 2),
            'exc': []
        },
    'Скрит Тест 6: ':
        {
            'ans': divisible_by_d([0,1,2,3,4,5,6,7,8,9,10], 1),
            'exc': [0,1,2,3,4,5,6,7,8,9,10]
        },
    'Скрит Тест 7: ':
        {
            'ans': divisible_by_d([2,3,5,9,10,15,16,20,24,25,27], 5),
            'exc': [5, 10, 15, 20, 25]
        },
    }

    passed = int()

    print("Проблем 1 тестове: \n")
    for test_name, test_results in fixed_tests.items():
        if test_results['ans'] != test_results['exc']:
            print(f'>>> {test_name} се провали!')

            if test_name.startswith('Тест'):
                print(f'    Очаквано: {test_results["exc"]}')
                print(f'    Получено: {test_results["ans"]}')
        else:
            passed += 1
            print(f'>>> {test_name} премина!')
        
    numbers = list(range(100))
    rnd_tests = 14
    for i in range(1, rnd_tests):
        rnd_d = floor(random() * 10) + 1
        ans = divisible_by_d(numbers[:], rnd_d)
        exc = [x for x in numbers if x%rnd_d == 0]
        if ans != exc:
            print(f">>> Случаен Тест {i}: се провали!")
            if (i <= 5):
                print(f'    Очаквано: {exc}')
                print(f'    Получено: {ans}')
        else:
            passed += 1
            print(f">>> Случаен Тест {i}: премина!")


    print(f"\nПроблем 1: {passed} от {len(fixed_tests) + rnd_tests - 1} преминати теста!")

# t = Timer(partial(test_problem_1))
# print(t.timeit(1))

s = time()
test_problem_1()
e = time()

print(F"Време: {int((e - s)*1000)} милесекунди.")
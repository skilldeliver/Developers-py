import os
import sys

from random import random, randint
from math import floor
from functools import partial, reduce
from timeit import Timer
from time import time, sleep

from problem_1 import divisible_by_d
from problem_2 import max_product
from problem_3 import b
from problem_4 import convert_fracts
from problem_5 import middle_permutation


class Test:
    def __init__(self):
        self.test_count = int()
        self.passed_count = int()

    def title(self, text: str) -> None:
        print(f'\n{text}\n')

    def equals(self, ans, exc, hidden: bool=False) -> None:
        self.test_count += 1

        if ans == exc:
            self.passed_count += 1
            print(f'>>> Тест {self.test_count}. премина!')
        else:
            print(f'>>> Тест {self.test_count}. се провали!')
            if not hidden:
                print(f'    Очаквано: {exc}')
                print(f'    Получено: {ans}')

    def results(self) -> tuple:
        return self.passed_count, self.test_count


def test_problem_1(disable_print=False):

    if disable_print:
        sys.stdout = open(os.devnull, 'w')

    print("Проблем 1: ")

    test = Test()
    test.title("Фиксирани тестове: ")

    test.equals(divisible_by_d([1,2,3,4,5,6], 2), [2,4,6])
    test.equals(divisible_by_d([1,2,3,4,5,6], 3), [3,6])
    test.equals(divisible_by_d([0,1,2,3,4,5,6], 4), [0,4])
    test.equals(divisible_by_d([0], 4), [0])
    test.equals(divisible_by_d([1,3,5], 2), [])

    test.equals(divisible_by_d([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10], hidden=True)
    test.equals(divisible_by_d([2,3,5,9,10,15,16,20,24,25,27], 5), [5, 10, 15, 20, 25], hidden=True)

    test.title("Случайни тестове: ")
    numbers = list(range(100))
    rnd_tests = 14

    for _ in range(1, rnd_tests):
        rnd_d = floor(random() * 10) + 1
        ans = divisible_by_d(numbers[:], rnd_d)
        exc = [x for x in numbers if x%rnd_d == 0]
        test.equals(ans, exc, hidden=True)

    passed, total = test.results()
    print(f"\nПроблем 1: {passed} от {total} преминати теста!")
    return  passed, total


def test_problem_2(disable_print=False):

    if disable_print:
        sys.stdout = open(os.devnull, 'w')

    print("Проблем 2: ")

    test = Test()
    test.title("Фиксирани тестове: ")

    test.equals(max_product([4,3,5], 2), 20)
    test.equals(max_product([10,8,7,9], 3), 720)
    test.equals(max_product([10,2,3,8,1,10,4], 5), 9600)
    test.equals(max_product([-4,-27,-15,-6,-1],2), 4)
    test.equals(max_product([10,3,-27,-1], 3), -30)


    test.equals(max_product([8,6,4,6], 3), 288, hidden=True)
    test.equals(max_product(list(range(10, -1, -1)), 5), 10*9*8*7*6, hidden=True)
    test.equals(max_product([13,12,-27,-302,25,37,133,155,-1], 5), 247895375, hidden=True)
    test.equals(max_product([-17,-8,-102,-309],2), 136, hidden=True)
    test.equals(max_product([14,29,-28,39,-16,-48],4), -253344, hidden=True)

    test.title("Генерирани тестове: ")
    for _ in range(30):
        length = randint(3, 10**4)
        n = [randint(-10**6, 10**6) for _ in range(length)]
        k = randint(1, length)
        test.equals(max_product(n, k), reduce(lambda x, y: x * y, sorted(n)[-k:]), hidden=True)

    passed, total = test.results()
    print(f"\nПроблем 2: {passed} от {total} преминати теста!")
    return passed, total


def test_problem_3(disable_print=False):
    if disable_print:
        sys.stdout = open(os.devnull, 'w')

    print("Проблем 3: ")

    test = Test()
    test.title("Фиксирани тестове: ")

    test.equals(b == False and b == True, True)

    passed, total = test.results()
    print(f"\nПроблем 3: {passed} от {total} преминати теста!")
    return passed, total


def test_problem_4(disable_print=False):
    if disable_print:
        sys.stdout = open(os.devnull, 'w')

    print("Проблем 4: ")

    test = Test()
    test.title("Фиксирани тестове: ")

    a = [[1, 2], [1, 3], [1, 4]]
    b = [[6, 12], [4, 12], [3, 12]]
    test.equals(convert_fracts(a), b)
    a = []
    b = []
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[2, 7], [1, 3], [1, 12]]
    b = [[24, 84], [28, 84], [7, 84]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[69, 130], [87, 1310], [3, 4]]
    b = [[18078, 34060], [2262, 34060], [25545, 34060]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[77, 130], [84, 131], [3, 4]]
    b = [[20174, 34060], [21840, 34060], [25545, 34060]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[6, 13], [187, 1310], [31, 41]]
    b = [[322260, 698230], [99671, 698230], [527930, 698230]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[8, 15], [7, 111], [4, 25]]
    b = [[1480, 2775], [175, 2775], [444, 2775]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[1, 1], [3, 1], [4, 1], [5, 1]]
    b = [[1, 1], [3, 1], [4, 1], [5, 1]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[1, 100], [3, 1000], [1, 2500], [1, 20000]]
    b = [[200, 20000], [60, 20000], [8, 20000], [1, 20000]]
    test.equals(convert_fracts(a), b, hidden=True)
    a = [[27115, 5262], [87546, 11111111], [43216, 255689]]
    b = [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]] 
    test.equals(convert_fracts(a), b, hidden=True)

    passed, total = test.results()
    print(f"\nПроблем 4: {passed} от {total} преминати теста!")
    return passed, total

def test_problem_5(disable_print=False):
    if disable_print:
        sys.stdout = open(os.devnull, 'w')

    test = Test()
    test.title("Фиксирани тестове: ")

    test.equals(middle_permutation("abc"),"bac")
    test.equals(middle_permutation("abcd"),"bdca")
    test.equals(middle_permutation("abcdx"),"cbxda")
    test.equals(middle_permutation("abcdxg"),"cxgdba")
    test.equals(middle_permutation("abcdxgz"),"dczxgba")


    sol = lambda s: (lambda s,i: "".join(s[i:i+(2 if len(s)%2 else 1)]+s[:i]+s[i+(2 if len(s)%2 else 1):]))(sorted(s,reverse=True),len(s)//2)
    base=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    test.title("Генерирани тестове: ")
    for _ in range(40):
        s="".join(sorted(base,key=lambda a: random())[:randint(2,len(base))])
        test.equals(middle_permutation(s),sol(s), hidden=True)

    passed, total = test.results()
    print(f"\nПроблем 5: {passed} от {total} преминати теста!")
    return passed, total


def main():
    tests = [test_problem_1, test_problem_2, test_problem_3, test_problem_4, test_problem_5]

    if len(sys.argv) >= 2:
        number = int(sys.argv[1])

        if number in [1, 2, 3, 4, 5]:
            s = time()
            tests[number - 1]()
            e = time()

            if int(e - s) > 7:
                print("Ъггхх! Решението е твърде бавно, нужни са повече от 7 секунди!")
    else:
        result = 0
        for i, test in enumerate(tests):
            s = time()
            passed, total = test(disable_print=True)
            e = time()

            sys.stdout = sys.__stdout__
            if int(e - s) > 7:
                print(f"Решението на Проблем {i+1}. е твърде бавно, нужни са повече от 7 секунди!")
            else:
                result += int(passed * (20 / total))
                print(f"Проблем {i+1}. {passed} от {total}. {result}%!")

        print(f"\nФинален резултат: {result} процента!")
        print(f"Не забрявай да се похвалиш или оплачеш във ФБ групата Developers. py")

if __name__ == '__main__':
    main()

# Problem Solving
#TODO
ДОБАВИ ЛИНК ПОД ВСЕКИ ПРОБЛЕМ КЪМ SOURCE-FILE: "КЪМ НЕГО"
МОЖЕ БИ ВКЛЮЧИ СКРИНШОТИ ЗА ТЕСТВАНЕТО И ПУБЛИКУВАНЕТО

Подбрани задачи за Фейсбук групата **Developers.py**.
Обща дейност за сформиране на активна **Python българска общност**.

`Ще бъде публикувана класация на най-добре представилите се.`

`Задачите не са авторски, а подбрани и преведени.` 

# Таблица на съдържанието
1. [ Решаване ](#Решаване)
1. [ Тестване на решенията ](#Тестване-на-решенията)
1. [ Публикуване на решенията ](#Публикуване-на-решенията)
1. [ Проблем 1 ](#Проблем-1)
1. [ Проблем 2 ](#Проблем-2)
1. [ Проблем 3 ](#Проблем-3)
1. [ Проблем 4 ](#Проблем-4)
1. [ Проблем 5 ](#Проблем-5)


## **Решаване**
Всеки проблем се намира в отделен **.py** файл.
Във всеки файл единствено е разписана сигнатурата на функцията. 
Вашето решение се състои в това да попълните тялото й.

#### За да преминете към решаване:
1. Клонирайте repository-то локално **git clone** https://github.com/skilldeliver/Developers-py.git
1. Преминете към решаване и тестване

## **Тестване на решенията**
Включени са тестове за всички описани проблеми.
Ако изпълните команда за тестване на единичен проблем на конзолата ще получите информация
за всеки тестов случай. Някои от тестовите случаи са скрити и разбирате единствено дали е преминал или не.
Ако изпълните команда за всички проблеми ще получите информация за оценката след всеки проблем и финалния резултат.

#### За да тествате само едно от решенията:

1. Oтворете терминала в клонирата директория.
1. Изпълнете командата **py tests.py n**, където **n** e номера на теста от [1,5]

#### За да тествате всички решения и получите краен резултат:

1. Oтворете терминала в клонирата директория.
1. Изпълнете командата **py tests.py**

## **Публикуване на решенията**
Единствения начин да разберем, че резултатът е достоверен е като видим решенията на всеки проблем.

#### За целта:

1. **Fork**-нете това repository
1. Във вашия **fork** решенията ги добавете в отделна директория с вашия **GitHub nickname**
1. Изпратете **pull requst**

## **Проблем 1**
Намерете всички числа от редицата **n**, които са делими на числото **d** без остатък.

#### `Вход:`
```python
n: list<int>
d: int
```

#### `Изход:`
```python
list<int> числата от n, делими на d без остатък
```

#### `Пример:`
```python

n = [1, 2, 3, 4, 5, 6]
d = 2
# числата, които са делими на 2 без остатък са: 2, 4 и 6:
return [2, 4, 6]

# Някои тестове:
"""
[1,2,3,4,5,6], 3   -> [3,6]
[0,1,2,3,4,5,6], 4 -> [0,4]
[0], 4             -> [0]
[1,3,5], 2         -> []
"""
```

## **Проблем 2**
Намерете максималното произведение на подредица(с дължина **k**) на редицата **n**.

#### `Вход:`
```python
n: list
k: int

len(n) >= 3
```

#### `Изход:`
```python
int най-голямото произведение на подредица[k] на редицата n
```

#### `Пример:`
```python

n = [4, 3, 5]
k = 2
# Подредиците на n с дължина k са [4, 3], [4, 5], [3, 5]
# произведенията на елементите са   12      20      15
return 20

# Някои тестове:
"""
[8, 10 , 9, 7], 3          -> 720
[10, 8, 3, 2, 1, 4, 10], 5 -> 9600
[-4, -27, -15, -6, -1], 2  -> 4
[10, 3, -1, -27] , 3       -> -30
"""
```


## **Проблем 3**
_Булевата на Шрьодингер._
Дефинирайте променлива **b**, така че следната кондиция да e **True**
```python
b == True and b == False
```

## **Проблем 4**
Намерете дробите получени от привеждането под общ знаменател на подадените рационални числа **q**.

#### `Бележка:`
```
Очаквайте големи числа.
```

#### `Вход:`
```python
q: list
# (q е двуизмерен list,
#  всеки вложен list съдържа само два int елемента - числител и знаменател)
```

#### `Изход:`
```python
list дробите получени от привеждането под общ знаменател
# (Трябва да е двуизмерен list,
#  всеки вложен list съдържа само два int елемента - числител и знаменател)
```
#### `Пример:`
```python

q = [[1, 2], [1, 3], [1, 4]]
# Общия знаменател на дробите е:
12
# следователно дробите, които се получават след привеждане са:
return [[6, 12], [4, 12], [3, 12]]
```

## **Проблем 5**
Намерете средния елемент от азбучно подредена редица получена от пренареждането на буквите в подадения **string**.
Ако дължината на редицата е четна, нека средният елемент бъде **n/2**, където **n** e дължината на редицата.

#### `Вход:`
```python
s: str
2 <= len(s) <= 26
# (Не съдържа повтарящи се елементи)
```

#### `Изход:`
```python
str средната пермутация на s: str
# (Не съдържа повтарящи се елементи)
```

#### `Пример:`
```python

s = 'abc'
# Азбучно подредени пермутации на s са:
{'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
# Редица е с четна дължина (6) следователно отговора е 3-тия елемент 'bac' (6/2)
return 'bac'

# Някои от тестовте:
"""
"abcd"    -> "bdca"
"abcdx"   -> "cbxda"
"abcdxg"  -> "cxgdba"
"abcdxgz" -> "dczxgba"
"""
```

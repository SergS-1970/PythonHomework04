# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

maxDegreeOfAPolynomial = int(
    input('Введите максимальный показатель степени многочлена К: '))
koefs = list()
for i in range(0, maxDegreeOfAPolynomial + 1):
    koefs.append(randint(0, 101))

expressionPolynomial  = list()
for i in range(len(koefs)):
    expressionPolynomial.append(f'{koefs[i]}*x**{maxDegreeOfAPolynomial}')
    flag = randint(0, 1)
    if flag == 1:
        expressionPolynomial.append(' + ')
    elif flag == 0:
        expressionPolynomial.append(' - ')
    maxDegreeOfAPolynomial -= 1

expressionPolynomial.pop(-1)
expressionPolynomial.append(' = 0')
print(expressionPolynomial)
print(''.join(expressionPolynomial))
fout = open('task4.txt', 'w')
fout.write(''.join(expressionPolynomial))
fout.close()

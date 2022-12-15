# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def calculationPi(accuracy):
    pi = 3
    decimalPlaces = 10**-accuracy    
    significant = 4
    value = 1
    while decimalPlaces < abs(value):
        value = 4 / significant / (significant - 1) / (significant - 2)
        if significant % 4 != 0:
            value *= -1
        pi += value
        significant += 2
    return round(pi, accuracy)


accuracy = int(input(
    'Введите количество цифр после запятой, которые нужно определить в числе Пи: '))
pi = calculationPi(accuracy)
print(f'Число Пи с точностью до {accuracy}-го знака равно:  {pi}')

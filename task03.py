# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input("Введите числа через пробел:  ").split()))
new_numbers = []

for i in numbers:
    if numbers.count(i) == 1:
        new_numbers.append(i)
print(f"Неповторяющимися элементами исходной числовой последовательности {numbers} являются: \n    {new_numbers}")

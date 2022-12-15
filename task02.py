#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Укажите число N: "))
i = 2
primeFactors = []
originalNumber = number
while i**2 <= originalNumber:
    if number % i == 0:
        primeFactors.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {originalNumber} указаны в списке: {primeFactors}")
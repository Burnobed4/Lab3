#Задание 1
squares = [x**2 for x in range(1, 11)]
print("1. Квадраты чисел:", squares)

#Задание 2
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("2. Чётные числа:", even_numbers)

#Задание 3
words = ["python", "Java", "c++", "Rust", "go"]
filtered_words = [word.upper() for word in words if len(word) > 3]
print("3. Отфильтрованные слова:", filtered_words)

#Задание 4
class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        current = self.n
        while current >= 1:
            yield current
            current -= 1


print("4. Вывод:")
for x in Countdown(5):
    print(x, end=" ")

#Задание 5
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\n5. Числа Фибоначчи:")
for num in fibonacci(5):
    print(num, end=" ")
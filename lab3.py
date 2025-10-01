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
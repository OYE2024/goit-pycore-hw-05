def caching_fibonacci():
    """
    Функція caching_fibonacci створює та використовує кеш для зберігання і повторного 
    використання вже обчислених значень чисел Фібоначчі.
    """
    cache = {}

    def fibonacci(num):
        """
        Функція fibonacci обчислює значення задоного числа Фібоначчі.
        """
        nonlocal cache
        if num in cache:
            return cache[num]
        elif num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            cache[num] = fibonacci(num-1) + fibonacci(num-2)
            return cache[num]

    return fibonacci  # повертає функцію як об'єкт, але не викликає її


fib = caching_fibonacci()
# fib(10) теж саме що й fibonacci(10)
# результатом виклику функції caching_fibonacci() є функція fibonacci як об'єкт
print(fib(10))
print(fib(15))


# 1. 0+1 = 1
# 2. 1+0 = 1
# 3. 1+1 = 2
# 4. 2+1 = 3
# 5. 3+2 = 5
# 6. 5+3 = 8
# 7. 8+5 = 13

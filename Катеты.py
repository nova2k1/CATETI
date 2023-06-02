import time

def calculate_hypotenuse(a, b):
    """Функция для расчета гипотенузы по теореме Пифагора."""
    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    return hypotenuse

def time_execution(func):
    """Декоратор для вывода информации о запуске функции."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        print(f"Функция {func.__name__} запущена")
        print(f"Длины сторон: a = {args[0]}, b = {args[1]}")
        print(f"Результат: {result}")
        print(f"Время выполнения: {execution_time} секунд")
        
        return result
    
    return wrapper

@time_execution
def calculate_hypotenuse_with_logging(a, b):
    """Функция для расчета гипотенузы с использованием декоратора."""
    hypotenuse = calculate_hypotenuse(a, b)
    return hypotenuse

# Главная программа
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

result = calculate_hypotenuse_with_logging(a, b)
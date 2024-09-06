# Функция с параметрами по умолчанию
def print_params(a: int = 1, b: str = 'строка', c: bool = True):
    print(f'a = {a}, b = {b}, c = {c}')

print_params(b = 25)
print_params(c = [1, 2, 3])

# Функция с распаковкой параметров
def value_list(first: float, second: bool, third: str):
    print(f'first = {first}, second = {second}, third = {third}')

values_dict: dict = {'first': 0.8, 'second': False, 'third': 'Word'}

value_list(**values_dict)

# Распаковка + отдельные параметры
value_list_2: list = [[1, 15, 36], 'Слово']

print_params(*value_list_2, 42)
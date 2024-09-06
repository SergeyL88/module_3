def print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

value_list: list = [False, [15, 'String', True], 'Word']
values_dict: dict = {'a': 0.8, 'b': False, 'c': 'Word'}
value_list_2: list = [[1, 15, 36], 'Слово']

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*value_list)
print_params(**values_dict)
print_params(*value_list_2, 42)

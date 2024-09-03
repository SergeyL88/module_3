calls :int = 0
# Функция подсчета вызовов
def count_calls() -> int :
    global calls
    calls += 1

# Функция подсчета символов , возврата слова в верхнем и нижнем регистре
def string_info(word: str) -> tuple :
    count_calls()
    return (len(word),word.upper(), word.lower())

# Функция проверки слова на совпадение с словом из списка
def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    contain: bool = False
    for word in list_to_search:
        if string.lower() == word.lower():
            contain = True
            break
    return contain



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


def calculate_structure_sum(elements):
    result = 0
    for element in elements:
        if isinstance(element, int):
            result += element
        elif isinstance(element, str):
            result += len(element)
        elif isinstance(element, dict):
            temp_list = []
            for key, value in element.items():
                temp_list.append(len(key) + value)
            result += calculate_structure_sum(temp_list)
        else:
            result += calculate_structure_sum(element)

    return result

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)

print(result)
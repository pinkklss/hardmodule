def calculate_structure_sum(data_structure):
    f_sum = 0
    if isinstance(data_structure, dict):
        for i, args in data_structure.items():
            f_sum += calculate_structure_sum(i)
            f_sum += calculate_structure_sum(args)
    elif isinstance(data_structure, (list, tuple, set)):
        for j in data_structure:
            f_sum += calculate_structure_sum(j)
    elif isinstance(data_structure, int):
        f_sum += data_structure
    elif isinstance(data_structure, str):
        f_sum += len(data_structure)
    return f_sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


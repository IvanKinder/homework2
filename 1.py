data_list = [1, 3.7, 'papa', 4 + 6j, type(1), None, [1, 2, 3], (3, 2, 1), {5, 2, 9, 4, 1},
             {1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}]

i = int(input(f"Введите номер элемента от 0 до {len(data_list) - 1}: "))

print (i, type(data_list[i]))

my_list = input("Введите элементы списка через пробел: ").split()
num_of_el = len(my_list)
i = 0
formated_list = []

while i < num_of_el:
    my_list.append(my_list[i + 1])
    my_list.append(my_list[i])
    i += 2

if num_of_el % 2 == 0:
    print (my_list[num_of_el:])
else:
    my_list.pop(-2)
    print (my_list[num_of_el:])

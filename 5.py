rate = input("Введите натуральные числа рейтинга через пробел: ").split()
sorted_rate = []
i = 0

for digit in rate:
    sorted_rate.append(int(digit))
    sorted_rate = sorted(sorted_rate)
    sorted_rate = sorted_rate[::-1]

new_el = int(input("Введите новый элемент рейтинга: "))

while True:
    if new_el >= sorted_rate[i]:
        sorted_rate.insert(i, new_el)
        break
    elif new_el < sorted_rate[-1]:
        sorted_rate.append(new_el)
        break
    else:
        i += 1

print (sorted_rate)

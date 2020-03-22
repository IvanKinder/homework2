products = []
i = 0
j = 0
k = []
characteristics = [[], [], [], []]
analitika = {}

while True:
    i += 1
    print ("\nДЛЯ ЗАВЕРШЕНИЯ ВВОДА НАЖМИТЕ q!\n")
    name = input("Введите название товара: ")
    if name == "q":
        break
    characteristics[0].append(name)
    cost = input("Введите цену товара: ")
    if cost == "q":
        break
    characteristics[1].append(cost)
    count = input("Введите количество товара: ")
    if count == "q":
        break
    characteristics[2].append(count)
    ed = input("Введите единицы измерения товара: ")
    if ed == "q":
        break
    characteristics[3].append(ed)
    products.append((i, {"название": name, "цена": cost, "количество": count, "ед": ed}))

for key in products[0][1].keys():
    k.append(key)

for j in range(len(k)):
    analitika[k[j]] = characteristics[j]

print (analitika)
month = int(input("Введите номер месяца от 1 до 12: "))
year_time = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
if 0 < month < 13:
    for key, value in year_time.items():
        if month in value:
            print (key)
else:
    print ("Надо было ввести от 1 до 12!!!")
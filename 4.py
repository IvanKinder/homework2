words = input("Введите несколько слов через пробел: ").split()

for word in enumerate(words, 1):
    print (f"{word[0]}. {word[1][:10]}")

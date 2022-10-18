were = input("Введите строку\nПрограмма перевернёт в ней все слова, в которых 5 и более букв:)\n").split()


def werewolves_generator(were):
    for word in were:
        if len(word) >= 5:
            intermediate = [letter for letter in word]
            intermediate.reverse()
            word = ""
            for each_letter in intermediate:
                word += each_letter
            yield word
        else:
            yield word


result = ""
for i in werewolves_generator(were):
    result += f"{i} "

print(result)

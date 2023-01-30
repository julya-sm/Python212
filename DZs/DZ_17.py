
# Поскольку задание 1 практически сделано на занятии, объединю 1 и 2 в одно. Для универсальности )


def search_letter_ind(sentence, letter):
    count = 0
    ind1 = sentence.find(letter)
    ind2 = sentence.rfind(letter)

    if ind1 != -1:
        count += 1
    if ind2 != -1:
        count += 1

    if count < 2:
        return "В предложении недостаточное количество указанной буквы"
    else:
        return ind1, ind2


print(search_letter_ind('крокодил', 'э'))
print()

s = 'I am learning Python. hello, WORLD!'
t = search_letter_ind(s, 'h')
first = t[0]
sec = t[1]

# удалить буквы, начиная с первого по последнее вхождение включительно

new_str1 = s[:first] + s[sec+1:]
print(new_str1)

# развернуть наоброт символы между первым и последним вхождением h

res = s[first+1:sec]
new_str2 = s[0:first+1] + res[::-1] + s[sec:]
print(new_str2)

# Задача 3 Найти в строке указанную подстроку и заменить ее на новую. Данные вводит пользователь

main_str = input('Строка: ')
sub_str1 = input('Ее заменяемая подстрока: ')
sub_str2 = input('Новая подстрока: ')
changed_str = main_str.replace(sub_str1, sub_str2)
print(changed_str)

# Задача 4

rhyme = "Ежевику для ежат\nПринесли два ежа.\nЕжевику еле-еле\nЕжата возле ели съели"
print(rhyme)
change_rhyme = rhyme.replace('\n', ' ')
count1 = 0
if change_rhyme.lower().startswith("е"):
    count1 += 1
print("Количество слов, начинающихся на 'е':", (change_rhyme.lower().count(' е') + count1))

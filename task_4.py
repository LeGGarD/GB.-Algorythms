"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
import string

l1 = input("Input a letter: ").lower()
l2 = input("Input a letter: ").lower()
if l1 in string.ascii_lowercase:  # Решил добавить проверки на то, что введена имеено латинская буква
    if l2 in string.ascii_lowercase:
        pos1 = string.ascii_lowercase.index(l1) + 1
        pos2 = string.ascii_lowercase.index(l2) + 1
        diff = abs(pos1 - pos2)
        if diff == 1:  # Если между буквами нет других - пишется немного другой вывод
            print(f"first letter is in position {pos1}\nsecond letter is in position {pos2}\n"
                  f"these letters stay back to back")
        else:
            print(f"first letter is in position {pos1}\nsecond letter is in position {pos2}\n"
                  f"there are {diff} letters between those, you've inputted")
    else:
        print("input a letter this time please")
else:
    print("input a letter this time please")

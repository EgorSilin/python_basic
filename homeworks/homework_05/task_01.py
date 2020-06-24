"""1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

if __name__ == "__main__":

    user_str_lst = []
    while True:
        user_str = input("Введитестроку для записи в файл:")
        if user_str:
            user_str_lst.append(user_str + "\n")
        else:
            break

    try:
        with open("text_01.txt", "w", encoding='utf-8') as f_obj:
            f_obj.writelines(user_str_lst)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

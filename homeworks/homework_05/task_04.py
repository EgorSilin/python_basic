"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

if __name__ == "__main__":
    # read file to strings list
    try:
        with open("text_04.txt", "r", encoding='utf-8') as f_obj:
            content_str_list = f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    # split strings list to word lists
    content_word_list = [el_str_list.split() for el_str_list in content_str_list]

    # change eng num to rus and join words in strings
    out_content_str_list = []
    for el_content_word_list in content_word_list:
        if el_content_word_list[0] == "One":
            el_content_word_list[0] = "Один"
        elif el_content_word_list[0] == "Two":
            el_content_word_list[0] = "Два"
        elif el_content_word_list[0] == "Three":
            el_content_word_list[0] = "Три"
        elif el_content_word_list[0] == "Four":
            el_content_word_list[0] = "Четыре"
        out_content_str_list.append(' '.join(el_content_word_list) + "\n")

    # write new strings in new file
    try:
        with open("text_04_new.txt", "w", encoding='utf-8') as f_obj:
            f_obj.writelines(out_content_str_list)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

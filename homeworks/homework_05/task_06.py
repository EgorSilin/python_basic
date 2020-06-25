"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def str_to_name(str_par):
    """take str and return class name"""
    content_word_list = str_par.split()[0][:-1]
    return content_word_list


def str_to_num_list(str_par):
    """Taking string with numbers and return list of int numbers

    :param str_par: string
    :return: list
    """
    str_par_len = len(str_par)
    num_sum = 0
    i = 0
    # parse string by symbol cycle
    while i < str_par_len:
        num_str = ''
        current_symbol = str_par[i]

        # check near num symbol cycle
        while '0' <= current_symbol <= '9':
            num_str += current_symbol
            i += 1
            if i < str_par_len:
                current_symbol = str_par[i]
            else:
                break

        i += 1
        if num_str != '':
            num_sum += int(num_str)

    return num_sum


if __name__ == "__main__":
    try:
        with open("text_06.txt", "r", encoding='utf-8') as f_obj:
            content_str_list = f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    class_dict = {str_to_name(el): str_to_num_list(el) for el in content_str_list}
    print(class_dict)

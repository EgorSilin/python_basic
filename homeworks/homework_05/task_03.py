"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

if __name__ == "__main__":
    try:
        with open("text_03.txt", "r", encoding='utf-8') as f_obj:
            content = f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    content_double_list = [content_str.split() for content_str in content]

    sum_salary = 0
    low_paid_family = []
    for pair in content_double_list:
        sum_salary += int(pair[1])
        if int(pair[1]) < 20:
            low_paid_family.append(pair[0])

    print(f"Средний оклад работников составляет {sum_salary/len(content_double_list)} тыс.")
    print(f"Следующие работники имеют оклад ниже 20 тыс.: {low_paid_family}")

"""7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json

if __name__ == "__main__":
    try:
        with open("text_07.txt", "r", encoding='utf-8') as f_obj:
            content_str_list = f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    profit_dict_list = []
    sum_profit = 0
    count_profit = 0
    for content_str in content_str_list:
        content_word_list = content_str.split()
        company_name = content_word_list[0]
        company_profit = (int(content_word_list[2]) - int(content_word_list[3]))
        if company_profit > 0:
            sum_profit += company_profit
            count_profit += 1
        profit_dict_list.append({company_name: company_profit})
    average_profit = sum_profit / count_profit
    profit_dict_list.append({'average_profit': average_profit})
    print(profit_dict_list)

    try:
        with open("json_07.json", "w") as out_obj:
            json.dump(profit_dict_list, out_obj)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

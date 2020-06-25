"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


if __name__ == "__main__":
    try:
        with open("text_02.txt", "r", encoding='utf-8') as f_obj:
            content = f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    print(f"Количество строк в файле равно {len(content)}.")
    for i, content_str in enumerate(content):
        print(f"В строке №{i} количество слов равно {len(content_str.split())}.")

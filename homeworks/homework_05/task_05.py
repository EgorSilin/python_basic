"""5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

if __name__ == "__main__":

    # write string of numbers in file
    try:
        with open("text_05.txt", "w", encoding='utf-8') as f_obj:
            f_obj.writelines("100 1 2 3 4 5 6 7 8 9")
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    # read strings of numbers from file
    try:
        with open("text_05.txt", "r", encoding='utf-8') as f_obj:
            content_str_list = f_obj.readline()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    # calc and print sum
    content_num_list = content_str_list.split()
    nums = [int(num) for num in content_num_list]
    print(sum(nums))

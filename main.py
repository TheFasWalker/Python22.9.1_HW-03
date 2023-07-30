# input_data = '2 5 7 9 11 15 20 55 110'


input_data = input('Введите неограниченное число цифр (положительные\отрицательные\с плавающей точкой) разделенные пробелом:')


def string_to_list(string):
    input_data_list = []
    length = len(string)
    next_is_number = True
    for i in range(0, length):
        if string[i] != ' ':
            if next_is_number:
                num = string[i]
                next_num_index = i + 1
                if next_num_index >= length:
                    input_data_list.append(num)
                    break

                if next_num_index <= length:
                    if string[next_num_index] != ' ' and string[next_num_index]:
                        for j in range(next_num_index, length):
                            next_element = string[j]
                            if next_element != ' ':
                                if next_element == ',':
                                    next_element = '.'
                                num = num + next_element
                            else:
                                break
                    input_data_list.append(num)
                next_is_number = False
        else:
            next_is_number = True

    return input_data_list


def format_strings_to_numbers():
    input_data_list_numbers = []
    for number_from_list in string_to_list(input_data):
        try:
            new_number = int(number_from_list)
            input_data_list_numbers.append(new_number)
            continue
        except:
            try:
                new_number = float(number_from_list)
                input_data_list_numbers.append(new_number)
                continue
            except:
                print(
                    f'Error of input data!  >>  {number_from_list} << не является числом. В итоговых расчетах учитываться небудет')
            finally:
                continue

        finally:
            continue

    return input_data_list_numbers


def sort_data_low_to_top(data):
    for i in range(0, len(data)):
        x = data[i]
        idx = i
        while idx > 0 and data[idx - 1] > x:
            data[idx] = data[idx - 1]
            idx -= 1
        data[idx] = x
    return data


sorted_data_list = sort_data_low_to_top(format_strings_to_numbers())
input_data = input('Введите число с которым будут проходить вычисления(положительное\отрицательное\с плавающей точкой):')
# input_data = '50'

input_data_formatted = string_to_list(input_data)


def format_single_string_to_number(number):
    try:
        num = int(number[0])
        return num
    except:
        try:
            num = float(number[0])
            return num
        except:
            print(f'выполнение поиска невозможно. {number[0]} не подходит под условия задачи')
    finally:
        pass


input_data_number = format_single_string_to_number(input_data_formatted)

print(f'Cписок введенных вами отсортированных чисел: \n{sorted_data_list} \n')


def binary_search(array, element, left, right):
    if left > right:
        print(f'точных совпадении во входящих данных ненайдено')
        if array[0] > element:
            print(f'число выходит за рамки входящих данных. Ближайшее большее число - первое из входящего списка {array[0]}')
        elif array[len(array)-1] < element:
            print(f'число выходит за рамки входящих данных. Ближайшее меньшее число - последнее из входящего списка {array[len(array)-1]}')
        else:
            for i in range(0, len(array)-1):
                if array[i] < element < array[i + 1]:
                    print(f'Ближайшее меньшее число {array[i]} его индекс {i}')
                    print(f'Ближайшее большее число {array[i+1]} его индекс {i+1}')

        return

    middle = (right + left) // 2
    if array[middle] == element:
        prev_number = middle - 1
        next_number = middle + 1
        if prev_number < 0:
            prev_number_message = 'Первее этого числа ничего нет ( оно первое)'
        else:
            prev_number_message = f'Ближайшее меньшее число = {sorted_data_list[middle - 1]} \nего индекс = {prev_number}'
        if next_number >= len(array):
            next_number_message = f'Следующего числа нет \nчисло {element} последнее'
        else:
            next_number_message = f'Ближайшее большее число = {sorted_data_list[middle + 1]} \nего индекс = {next_number}'
            pass
        print(f'Искомое число {element} найдено')
        print(prev_number_message)
        print(next_number_message)
        return middle

    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


binary_search(sorted_data_list, input_data_number, 0, len(sorted_data_list)-1)

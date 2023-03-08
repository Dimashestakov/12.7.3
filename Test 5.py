def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


input_str = input("Введите последовательность чисел : ")
try:
    numbers = [int(num) for num in input_str.split()]
except ValueError:
    print("Ошибка: некорректный ввод данных")
    exit()

target_num_str = input("Введите любое число: ")
try:
    target_num = int(target_num_str)
except ValueError:
    print("Ошибка: некорректный ввод данных")
    exit()

sorted_numbers = sorted(numbers)
pos = binary_search(sorted_numbers, target_num)
if pos == len(sorted_numbers):
    print("Введенное число больше всех чисел в последовательности")
elif pos == 0:
    print("Введенное число меньше всех чисел в последовательности")
else:
    print("Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу:",
          pos)
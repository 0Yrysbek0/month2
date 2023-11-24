# Функция bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
def binary_search(element, sorted_list):
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == element:
            return mid  # Элемент найден, возвращаем индекс
        elif guess < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Элемент не найден

# Пример использования:
element_to_find = 22
result = binary_search(element_to_find, sorted_list)
if result != -1:
    print(f"Элемент {element_to_find} найден по индексу {result}.")
else:
    print(f"Элемент {element_to_find} не найден.")
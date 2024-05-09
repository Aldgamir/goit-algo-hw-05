def binary_search(array, target):
  
  low = 0
  high = len(array) - 1
  count = 0

  while low <= high:
    mid = (low + high) // 2
    count += 1

    if array[mid] == target:
      return count, array[mid]
    elif array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  # Не знайдено
  return count, array[high]

# Перевіряємо правильність роботи на прикладі:
array = [1.2, 3.4, 5.6, 7.8, 9.1, 10.3, 11.4]
target = 5.6

count, upper_bound = binary_search(array, target)

print(f"Кількість ітерацій: {count}")
print(f"Верхня межа: {upper_bound}")

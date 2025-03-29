
# # O(1)
# lista_numeros = [4,6,8,9,10]
# variable = lista_numeros[2]
# print(variable)

# # O(log n)
# def binary_search(array, target):
#     left, right = 0, len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# lista_numeros = [5,6,4,32,1,2,3]
# lista_numeros.sort()
# print(lista_numeros)
# print("indice: ",binary_search(lista_numeros,3))

# # O(n)
# arreglo = ["c","o","d","i","n","g"]
# objetivo = "i"
# for i in range(len(arreglo)):
#     if objetivo == arreglo[i]:
#         print("encontrado")
#         break
#     print("next")

# # O(n log n)
# def merge_sort(array):
#     if len(array) > 1:
#         mid = len(array) // 2
#         left_half = array[:mid]
#         right_half = array[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 array[k] = left_half[i]
#                 i += 1
#             else:
#                 array[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             array[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             array[k] = right_half[j]
#             j += 1
#             k += 1

# mi_lista = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(mi_lista)
# print("Lista ordenada:", mi_lista)

# # O(n^2)
# def bubble_sort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]

# mi_lista = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(mi_lista)
# print("Lista ordenada:", mi_lista)

# # O(2^n)
# def knapsack(weights, values, capacity):
#     n = len(weights)
    
#     def knapsack_recursive(i, remaining_capacity):
#         if i == n or remaining_capacity == 0:
#             return 0
#         if weights[i] > remaining_capacity:
#             return knapsack_recursive(i + 1, remaining_capacity)
#         else:
#             include_item = values[i] + knapsack_recursive(i + 1, remaining_capacity - weights[i])
#             exclude_item = knapsack_recursive(i + 1, remaining_capacity)
#             return max(include_item, exclude_item)
    
#     return knapsack_recursive(0, capacity)

# # Ejemplo de uso
# weights = [1, 2, 3, 4]
# values = [10, 20, 30, 40]
# capacity = 5
# max_value = knapsack(weights, values, capacity)
# print("Valor máximo:", max_value)

# O(n!)
def permute(arr):
    result = []
    if len(arr) == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permute(rest):
            result.append([elem] + p)
    return result

# Ejemplo de uso
mi_lista = [1, 2, 3, 2, 3,2, 3,2, 3, 2, 3,2, 3,2, 3]
permutaciones = permute(mi_lista)
for p in permutaciones:
    print(p)


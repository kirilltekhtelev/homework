#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Enter N: '))
arr = [int(input('Enter elem: ')) for i in range(n)]
x = int(input('Enter X: '))
_arr = []
for i in arr:
    _arr.append(abs(x-i))
indexOfNearElem = _arr.index(min(_arr))
print(arr[indexOfNearElem])
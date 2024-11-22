def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        small_num = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[small_num]:
                small_num = j
        alist[i], alist[small_num] = alist[small_num], alist[i]
    return alist



def binary_search(sorted_alist, value):
    n = len(sorted_alist)
    result_ok = False
    first = 0
    last = n - 1
    while first < last:
        middle = (first + last) // 2
        if value == sorted_alist[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
        elif value > sorted_alist[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok == True:
        print(f"Элемент найден")
        print(pos)
    else:
        print('Элемент не найден')






usorted_list = [1, 4, 6, 3, 2, 9]
sorted_list = selection_sort(usorted_list)

binary_search(sorted_list,9)



















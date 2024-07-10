def get_matrix(n, m, value):
    i = 1
    j = 1
    list1 = []
    list2 = []
    while i <= n:
        while j <= m:
            list2.append(value)
            j = j + 1
        list1.append(list2)
        i = i + 1
    return list1


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

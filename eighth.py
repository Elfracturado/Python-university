def is_increasing(row):
    for i in range(len(row) - 1):
        if row[i] > row[i + 1]:
            return False
    return True

def is_decreasing(row):
    for i in range(len(row) - 1):
        if row[i] < row[i + 1]:
            return False
    return True

M, N = map(int, input("Введите M и N: ").split())
print("Введите матрицу:")
A = [list(map(int, input().split())) for _ in range(M)]
max_element = None
for row in A:
    if is_increasing(row) or is_decreasing(row):
        row_max = max(row)
        if max_element is None or row_max > max_element:
            max_element = row_max

if max_element is None:
    print("В матрице нет упорядоченных строк")
else:
    print("Максимальный элемент среди упорядоченных строк:", max_element)



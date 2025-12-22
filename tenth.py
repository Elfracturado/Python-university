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


# ---------- ВВОД ИЗ ФАЙЛА ----------
with open("Zvyagintsev_Nikita_Aleksandrovich_Um-252_vvod.txt", "r", encoding="utf-8") as f:
    M, N = map(int, f.readline().split())
    A = []
    for _ in range(M):
        A.append(list(map(int, f.readline().split())))

max_element = None

for row in A:
    if is_increasing(row) or is_decreasing(row):
        row_max = row[0]
        for x in row:
            if x > row_max:
                row_max = x
        if max_element is None or row_max > max_element:
            max_element = row_max

with open("Zvyagintsev_Nikita_Aleksandrovich_Um-252_vivod.txt", "w", encoding="utf-8") as f:
    if max_element is None:
        f.write("В матрице нет упорядоченных строк")
    else:
        f.write("Максимальный элемент среди упорядоченных строк: "
                + str(max_element))

M, N = map(int, input("Введите M и N: ").split())
print("Введите матрицу:")
D = []
for i in range(M):
    D.append(list(map(int, input().split())))
k = int(input("Введите номер строки k")) - 1
for j in range(N - 1):
    for p in range(N - j - 1):
        if D[k][p] > D[k][p + 1]:
            for i in range(M):
                D[i][p], D[i][p + 1] = D[i][p + 1], D[i][p]

print("Отсортированная матрица:")
for row in D:
    print(*row)

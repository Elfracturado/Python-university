with open("Zvyagintsev_Nikita_Aleksandrovich_Um-252_vvod.txt", "r", encoding="utf-8") as f:
    M, N = map(int, f.readline().split())
    D = []
    for _ in range(M):
        D.append(list(map(int, f.readline().split())))
    k = int(f.readline()) - 1

for j in range(N - 1):
    for p in range(N - j - 1):
        if D[k][p] > D[k][p + 1]:
            for i in range(M):
                D[i][p], D[i][p + 1] = D[i][p + 1], D[i][p]

with open("Zvyagintsev_Nikita_Aleksandrovich_Um-252_vivod.txt", "w", encoding="utf-8") as f:
    for row in D:
        f.write(" ".join(map(str, row)) + "\n")

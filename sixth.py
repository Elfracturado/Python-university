n = int(input("Введите количество элементов"))
print("Введите элементы")
arr = []
uniq_arr = []
found = False
for i in range(n):
    s = input()
    if uniq_arr.count(s) == 0:
        uniq_arr.append(s)
    else:
        found = True
    arr.append(s)
if found:
    for s in uniq_arr:
        c = arr.count(s)
        if c > 1:
            print(s, " повторён ", c, " раз(а).")
else:
    print("Повторов не найдено")
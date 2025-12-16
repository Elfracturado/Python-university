arr = []
res_arr = []
print("Введите 15 элементов")
for i in range(15):
    x = int(input())
    arr.append(x)
    if x < 10:
        res_arr.append(0)
    elif x > 20:
        res_arr.append(1)
    else:
        res_arr.append(x)
print(arr)
print(res_arr)
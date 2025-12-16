def findAbcNumbers(n, a, b, c):
    var1 = a * 100 + b * 10 + c
    var2 = a * 100 + c * 10 + b
    var3 = c * 100 + b * 10 + a
    var4 = b * 100 + a * 10 + c
    var5 = b * 100 + c * 10 + a
    var6 = c * 100 + a * 10 + b
    count = 0
    if 100 <= var1 <= n:
        count += 1
    if 100 <= var2 <= n:
        count += 1
    if 100 <= var3 <= n:
        count += 1
    if 100 <= var4 <= n:
        count += 1
    if 100 <= var5 <= n:
        count += 1
    if 100 <= var6 <= n:
        count += 1

    return count


def reversator(s):
    str = s.split(" ")
    new_str = ""
    for s in str:
        new_str = s + " " + new_str
    return new_str

print(findAbcNumbers(230, 1, 2, 3))
print(reversator("ta ta at at"))
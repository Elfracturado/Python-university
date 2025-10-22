n = int(input("введите n"))
k = int(input("введите k"))

fn = 1
fp = 0
res = 0
for i in range(1, n):
    ft = fn
    fn += fp
    fp = ft
    if i>=k:
        res+=fn

print(res)
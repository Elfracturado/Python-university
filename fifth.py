s = input("введите строку")
r = ""
strs = s.split(" ")
for str in strs:
    str1 = str.capitalize()
    r += str1 + " "
print(r)
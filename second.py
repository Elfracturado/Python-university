import math
x = float(input("введите x"))
y = float(input("введите y"))
z = float(input("введите z"))

s = math.pow(2, -x)*math.sqrt(x+math.pow(abs(y), 1/4))*math.pow(math.exp((x-1)/math.sin(z)), 1/3)

print("s = {0:.2f}".format(s))
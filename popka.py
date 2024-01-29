import math

f = open("output.txt", "wt")
for i in range(0, 21):
    print(f'факторіал {i} = {math.factorial(i)}', file = f)
f.close()


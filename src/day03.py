from utils.api import get_input

input_str = get_input(3)

freq = [0,0,0,0,0,0,0,0,0,0,0,0]

for l in input_str:
    for i in range(0, len(l)-1):
        if int(l[i]) == 1:
            freq[i] += 1

print(len(input_str))
isize = len(input_str)
print(freq)

gamma_rate = ""
for f in freq:
    if f > (isize/2):
        gamma_rate += "1"
    else:
        gamma_rate += "0"

print(int(gamma_rate, 2))
from utils.api import get_input

input_str = get_input(1)

input_ints = list(map(int, input_str))

prev = 99999999999
counter = 0
for l in input_str:
    if int(l) > prev:
        counter += 1
    prev = int(l)

print(counter)

counter = 0
prev = 99999999999

for i in range(1, len(input_ints)):
    measurewindows = sum(input_ints[(i-1):(i+2)])
    if measurewindows > prev:
        counter += 1
    prev = measurewindows

if measurewindows > prev:
    counter += 1

print(counter)
print(i)
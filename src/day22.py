from utils.api import get_input
import numpy as np

#input_str = get_input(22)
input_str = open("../inputs/22c").readlines()

values = []
for seq in input_str:
    for dimension in seq.split()[1].split(","):
        if dimension.startswith("x="):
            x_from = int(dimension[2:].split("..")[0])
            x_to = int(dimension[2:].split("..")[1])
        elif dimension.startswith("y="):
            y_from = int(dimension[2:].split("..")[0])
            y_to = int(dimension[2:].split("..")[1])
        elif dimension.startswith("z="):
            z_from = int(dimension[2:].split("..")[0])
            z_to = int(dimension[2:].split("..")[1])
    values.append(min(x_from, y_from, z_from))
    values.append(max(x_to, y_to, z_to))

print("Max: ", max(values), "Min: ", min(values))

xyz_size = max(values) + abs(min(values))

x_size = xyz_size
y_size = xyz_size
z_size = xyz_size
cube = np.zeros( (xyz_size, xyz_size, xyz_size), dtype=bool )

# Parsing
for seq in input_str:
    state = 1 if seq.split()[0] == "on" else 0
    for dimension in seq.split()[1].split(","):
        if dimension.startswith("x="):
            x_from = int(dimension[2:].split("..")[0]) + int(x_size/2)
            x_to = int(dimension[2:].split("..")[1]) + int(x_size/2)
        elif dimension.startswith("y="):
            y_from = int(dimension[2:].split("..")[0]) + int(y_size/2)
            y_to = int(dimension[2:].split("..")[1]) + int(y_size/2)
        elif dimension.startswith("z="):
            z_from = int(dimension[2:].split("..")[0]) + int(z_size/2)
            z_to = int(dimension[2:].split("..")[1]) + int(z_size/2)

    if x_from >= 0 and x_to < x_size:
        if y_from >= 0 and y_to < y_size:
            if z_from >= 0 and z_to < z_size:
                for x in range(x_from, x_to+1):
                    for y in range(y_from, y_to+1):
                        for z in range(z_from, z_to+1):
                            cube[x][y][z] = state
            else:
                print("Z bounds")
        else:
            print("Y bounds")
    else:
        print("X bounds")

print(cube.sum())

from utils.api import get_input
import numpy as np

input_str = open("../inputs/22c").readlines()


# Parsing
for seq in input_str:
    state = 1 if seq.split()[0] == "on" else 0
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
    if (x_from > x_to or y_from > y_to or z_from > z_to):
        print("Error on seq: " + seq)

    print(state, x_from, x_to, y_from, y_to, z_from, z_to)
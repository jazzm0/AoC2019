import sys

w = 25
t = 6
layers = {}
layer = []
layer_line = []
index_w = 0
index_t = 0
layer_index = 0
zero_count = sys.maxsize
zero_count_index = -1


def count_digits(lay, digit):
    count = 0
    for ll in lay:
        for d in ll:
            if d == digit:
                count += 1
    return count


with open('input') as ifile:
    for line in ifile:
        pixels = [int(x) for x in line[:-1]]

for digit in pixels:
    layer_line.append(digit)
    index_w += 1
    if index_w == w:
        index_w = 0
        index_t += 1
        layer.append(layer_line)
        layer_line = []

    if index_t == t:
        layers[layer_index] = layer
        actual = count_digits(layer, 0)
        if actual < zero_count:
            zero_count_index = layer_index
            zero_count = actual
        layer_index += 1
        layer = []
        index_w = 0
        index_t = 0

target_layer = layers[zero_count_index]

print(count_digits(target_layer, 1) * count_digits(target_layer, 2))

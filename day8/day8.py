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


def get_first_nt_pixel(layers, x, y):
    for l in range(len(layers)):
        if layers[l][x][y] != 2:
            return layers[l][x][y]


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
print('\n\n\n')
target_layer = []
for lay in range(len(layers)):
    for x in range(t):
        target_layer_line = []
        for y in range(w):
            pixel = get_first_nt_pixel(layers, x, y)
            target_layer_line.append(pixel)
        target_layer.append(target_layer_line)
count = 0
for lay in range(len(target_layer)):
    s = ''
    for i in range(len(target_layer[lay])):
        if target_layer[lay][i] == 0:
            s = s + ' '
        else:
            s = s + 'O'

    print(s)
    count += 1
    if count == t:
        break

from collections import Counter


WIDTH = 25
HEIGHT = 6
BLANK = "_"
BLACK = "X"
WHITE = " "


def generate_layers(image: str) -> list[str]:
    layers = []
    layer = ""
    pixel_count = 0
    for pixel in image:
        layer += pixel
        pixel_count += 1
        if pixel_count % (WIDTH * HEIGHT) == 0:
            layers.append(layer)
            layer = ""
    return layers


def print_image(image: str) -> None:
    print()
    for i in range(0, HEIGHT):
        print(image[WIDTH * i : WIDTH * (i + 1)])
    print()


def part_one(input_arr: list[str]) -> int:
    fewest_zeros = float("inf")
    ones_digits = twos_digits = 0
    for layer in generate_layers(input_arr[0]):
        c = Counter(layer)
        if c["0"] < fewest_zeros:
            fewest_zeros = c["0"]
            ones_digits = c["1"]
            twos_digits = c["2"]
    return ones_digits * twos_digits


def part_two(input_arr: list[str]) -> str:
    image_arr = [BLANK] * WIDTH * HEIGHT
    for layer in generate_layers(input_arr[0]):
        for i in range(len(layer)):
            if layer[i] == "0" and image_arr[i] == BLANK:
                image_arr[i] = WHITE
            elif layer[i] == "1" and image_arr[i] == BLANK:
                image_arr[i] = BLACK
    image = "".join(image_arr)
    print_image(image)
    return "See above"


input_arr: list[str] = open("advent_2019_day_08.txt").read().splitlines()

print("Advent of password 2019 - Day 08")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")

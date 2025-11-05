from advent_day import AdventDay
from collections import Counter

class Advent2019Day8(AdventDay):
    WIDTH = 25
    HEIGHT = 6
    BLANK = '_'
    BLACK = 'X'
    WHITE = ' '

    def _generate_layers(self, image: str) -> list[str]:
        layers = []
        pixel_count = 0
        layer = ''
        for pixel in image:
            layer += pixel
            pixel_count += 1
            if pixel_count % (self.WIDTH * self.HEIGHT) == 0:
                layers.append(layer)
                layer = ''
        return layers

    def _print_image(self, image: str) -> None:
        print()
        for i in range(0, self.HEIGHT):
            print(image[self.WIDTH * i:self.WIDTH * (i+1)])
        print()


    def part_one(self) -> int:
        ones_digits = twos_digits = 0
        layers = self._generate_layers(self.input_str_array[0])

        fewest_zeros = float('inf')
        ones_digits = twos_digits = 0
        for layer in layers:
            c = Counter(layer)
            if c['0'] < fewest_zeros:
                fewest_zeros = c['0']
                ones_digits = c['1']
                twos_digits = c['2']
        return ones_digits * twos_digits

    def part_two(self) -> str:
        layers = self._generate_layers(self.input_str_array[0])
        image_arr = [self.BLANK] * self.WIDTH * self.HEIGHT
        for layer in layers:
            for i in range(len(layer)):
                if layer[i] == '0' and image_arr[i] == self.BLANK:
                    image_arr[i] = self.WHITE
                elif layer[i] == '1' and image_arr[i] == self.BLANK:
                    image_arr[i] = self.BLACK
        image = ''.join(image_arr)
        self._print_image(image)
        return image


Advent2019Day8().run()
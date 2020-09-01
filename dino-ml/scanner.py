from PIL import Image
from datetime import datetime
import os
import uuid

dino_color = (83, 83, 83, 255)

def screenshot(x, y, w, h, f_name = None):
    #f_name = 'tmp-{0}.png'.format(datetime.utcnow().isoformat('-').replace(':', '-'))

    if f_name is None:
        f_name = 'tmp.png'

    os.system("screenshot.exe -rc {0} {1} {2} {3} -o {4}".format(x, y, w, h, f_name))
    img = Image.open(f_name)
    return img

def is_dino_color(pixel):
    return pixel == dino_color

def obstacle(distance, length, speed, time):
    return { 'distance': distance, 'length': length, 'speed': speed, 'time': time }

class Scanner:

    def __init__(self):
        self.dino_start = (0, 0)
        self.dino_end = (0, 0)
        self.last_obstacle = {}
        self.__current_fitness = 0
        self.__change_fitness = False

    def find_game(self):
        #image = screenshot(0, 0, 1500, 1500)
        #image = screenshot(650, 140, 1260, 280)
        image = screenshot(0, 280, 1500, 700)

        size = image.size
        pixels = []
        for y in range(0, size[1], 10):
            for x in range(0, size[0], 10):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    pixels.append((x, y))

        if not pixels:
            raise Exception("Game not found!")

        self.__find_dino(pixels)

    def __find_dino(self, pixels):
        start = pixels[0]
        end = pixels[1]
        for pixel in pixels:
            if pixel[0] < start[0] and pixel[1] > start[1]:
                start = pixel
            if pixel[0] > end[0] and pixel[1] > end[1]:
                end = pixel
        self.dino_start = start
        self.dino_end = end

    def find_next_obstacle(self):
        #image = screenshot(210, 100, 500, 155, f_name='next_obstacle.png')
        image = screenshot(110, 280, 1500, 700, f_name='next_obstacle.png')
        dist = self.__next_obstacle_dist(image)

        print('dist: {0}'.format(dist))

        if dist < 50 and not self.__change_fitness:
            self.__current_fitness += 1
            self.__change_fitness = True
        elif dist > 50:
            self.__change_fitness = False
        time = datetime.now()
        delta_dist = 0
        speed = 0
        if self.last_obstacle:
            delta_dist = self.last_obstacle['distance'] - dist
            speed = (delta_dist / ((time - self.last_obstacle['time']).microseconds)) * 10000
        self.last_obstacle = obstacle(dist, 1, speed, time)
        return self.last_obstacle

    def __next_obstacle_dist(self, image):

        s = 0
        MAX_WIDTH = image.width
        MAX_HEIGHT = image.height
        #for x in range(210, 250, 1):
        for x in range(95, 125, 1):
            for y in range(70, 100, 1):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    s += 1

        print (s)

        if s > 650:
            print('Game over!')
            raise Exception('Game over!')

        for x in range(0, MAX_WIDTH, 5):
            for y in range(80, 115, 5):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    return x

        return 1000000

    def reset(self):
        self.last_obstacle = {}
        self.__current_fitness = 0
        self.__change_fitness = False

    def get_fitness(self):
        return self.__current_fitness

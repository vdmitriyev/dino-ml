
from PIL import Image
from scanner import screenshot, is_dino_color
import uuid

# dino_color = (83, 83, 83, 255)

# def is_dino_color(pixel):
#     return pixel == dino_color

def __next_obstacle_dist():
    #image = Image.open("dino-big-sample.png")
    #image = Image.open("dino-big-sample-v2.png")
    image = Image.open("dino-big-sample-v3.png")

    #print(dir(image))
    print(image.width)
    print(image.height)
    s = 0
    for x in range(image.width):
        for y in range(image.height):
    #         print(x, y)
            #color = image.getpixel((x, y))
            color = image.getpixel((x, y))
            #print(color)
            if is_dino_color(color):
                s += 1
    print ('Pixels as dino: {0}'.format(s))
    print ('Total pixels: {0}'.format(image.width * image.height))

def main():
    __next_obstacle_dist()

    # test screenshots
    #print ('making screenshots of dino only')
    screenshot(80, 580, 208, 682, f_name = 'dino-big-{0}.png'.format(str(uuid.uuid1())[:8]))

if __name__ == '__main__':
    main()



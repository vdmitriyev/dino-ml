
from PIL import Image

dino_color = (83, 83, 83, 255)

def is_dino_color(pixel):
    return pixel == dino_color

def __next_obstacle_dist():
    image = Image.open("tmp-part.png")
    #print(dir(image))
    #print(image.width)
    #print(image.height)
    s = 0
    for x in range(210, 250, 1):
        for y in range(70, 100, 1):
    #         print(x, y)
            #color = image.getpixel((x, y))
            color = image.getpixel((x, y))
            # print(color)
            if is_dino_color(color):
                s += 1
    print (s)

def main():
    __next_obstacle_dist()

if __name__ == '__main__':
    main()


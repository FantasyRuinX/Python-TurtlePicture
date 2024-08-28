import turtle as window
from PIL import Image as img_data
import os

def get_pixel_info() -> tuple :

    print()
    for _,_,filename in os.walk("Pictures") :
        print(filename)

    name = input("Enter picture name with the extension : ")
    pixel_rgb = []

    if os.path.exists(f"Pictures/{name}") :
        print(f"{name} : Found")

        img = img_data.open(f"Pictures/{name}").convert("RGB")
        img_size = (img.width,img.height)

        for row in range(0,img_size[1]) :
            for cell in range(0,img_size[0]) :
                pixel_rgb.append(img.getpixel((cell,row)))

        return img_size, img
    
    else :
        print(f"{name} : Not Found")
        return (0,0), (0,0,0)

def draw_picture() -> None :
    img_size, img_pixel_data = get_pixel_info()
    pixel_num = 0

    for row in range(img_size[1]) :
        for cell in range(img_size[0]) :
            
            
            print(f"Pixels left to draw : {(img_size[0]*img_size[1]) - (pixel_num)}")
            pixel_num += 1

            window.penup()
            window.setpos((-img_size[0]) + (cell*2),(img_size[1]) - (row*2))
            window.pendown()

            img_rgb = img_pixel_data.getpixel((cell,row))
            window.color(img_rgb[0]/255,img_rgb[1]/255,img_rgb[2]/255)

            window.begin_fill()
            for _ in range(4) :
                window.forward(2)
                window.right(90)
            window.end_fill()


def main() :
    Commands = ("draw","off")

    window.title("Redraw picture")
    window.speed(0)
    #window.tracer(False)
    window.hideturtle()

    while True :
        window.update()

        print(f"Commands : {Commands}")
        cmd = input("Enter a command : ")

        match (cmd) :
            case "draw" :
                draw_picture()
            case "off" :
                break

main()
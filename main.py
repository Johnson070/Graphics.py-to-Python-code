from graphics import *
import main_menu as menu
import keyboard
from math import sqrt

picture = None

def draw_menu():
    global picture

    name = ''

    if draw_en[0]:
        name = 'menu.png'
    elif draw_en[1]:
        name = 'menu1.png'
    elif draw_en[2]:
        name = 'menu2.png'
    elif draw_en[3]:
        name = 'menu3.png'
    else:
        name = 'menu.png'

    img = Image(Point(1100, 500), name)
    picture = img
    img.draw(window)

    rect = Rectangle(Point(1050,175), Point(1150,275))
    rect.setFill(color)
    rect.setWidth(width)
    rect.setOutline(outline_color)
    rect.draw(window)

update_menu = False
objects = []
coords = []
out = []
polygon = []
temp_dots = []
draw_polygon = False
draw_en = [True,False,False,False]
back_en = False
color = ""
outline_color = "black"
width = 1
sw_color = True


window = GraphWin("Test",1200,1000)
menu.create_menu(window)
draw_menu()


out.append('''from graphics import *''')
out.append('''window = GraphWin("Test",1000,1000)''')
out.append('''''')

def mode_en(n):
    global coords
    global draw_en
    global update_menu

    coords = []
    draw_en = [False]*4
    draw_en[n] = True
    update_menu = True

def backk():
    global back_en

    back_en = True

def printt():
    global objects

    for i in out:
        if type(i) == list:
            for j in i:
                print(j)
        else:
            print(i)

def draw_pol():
    global draw_polygon

    draw_polygon = True

def color_sel():
    global color
    color = input("Input color(HEX(#______) or NAME): ")

def width_sel():
    global width

    try:
        width = int(input("Input width(int): "))
        if width == 0 or width > 20:
            width = 1
    except:
        print("ERROR!!!")
        width = 1

def outline_sel():
    global outline_color
    outline_color = input("Input outline color(HEX(#______) or NAME): ")

def switch_color_sel():
    global sw_color
    sw_color = not sw_color

keyboard.add_hotkey("1", lambda: mode_en(0))
keyboard.add_hotkey("2", lambda: mode_en(1))
keyboard.add_hotkey("3", lambda: mode_en(2))
keyboard.add_hotkey("4", lambda: mode_en(3))
# keyboard.add_hotkey("s", lambda: pol_stop())
#keyboard.add_hotkey("0", exit())
keyboard.add_hotkey("z", lambda: backk())
keyboard.add_hotkey("p", lambda: printt())
keyboard.add_hotkey("d", lambda: draw_pol())
keyboard.add_hotkey("c", lambda: color_sel())
keyboard.add_hotkey("w", lambda: width_sel())
keyboard.add_hotkey("o", lambda: outline_sel())
keyboard.add_hotkey("s", lambda: switch_color_sel())

def del_temp_dots():
    global temp_dots

    for i in temp_dots:
        i.undraw()
    temp_dots = []

def oval():
    global coords
    global window
    global out
    global color
    global width
    global outline_color

    if len(coords) == 2:
        cir = Circle(Point(coords[0][0], coords[0][1]), round(sqrt((coords[1][1]-coords[0][1])**2 + (coords[1][0]-coords[0][0])**2)))
        cir.setOutline(outline_color)
        cir.setFill(color)
        cir.setWidth(width)
        objects.append(cir)
        cir.draw(window)

        pre = []
        pre.append(f'''cir = Circle(Point({coords[0][0]}, {coords[0][1]}), {round(sqrt((coords[1][1]-coords[0][1])**2 + (coords[1][0]-coords[0][0])**2))})''')
        pre.append(f'''cir.setOutline("{outline_color}")''')
        pre.append(f'''cir.setFill("{color}")''')
        pre.append(f'''cir.setWidth({width})''')
        pre.append(f'''cir.draw(window)''')

        out.append(pre)
        coords = []
        del_temp_dots()
    else:
        return False

def rect():
    global coords
    global window
    global out
    global color
    global width
    global outline_color

    if len(coords) == 2:
        cir = Rectangle(Point(coords[0][0], coords[0][1]),Point(coords[1][0], coords[1][1]))
        cir.setOutline(outline_color)
        cir.setFill(color)
        cir.setWidth(width)
        objects.append(cir)
        cir.draw(window)
        pre = []
        pre.append(f'''cir = Rectangle(Point({coords[0][0]}, {coords[0][1]}),Point({coords[1][0]}, {coords[1][1]}))''')
        pre.append(f'''cir.setOutline("{outline_color}")''')
        pre.append(f'''cir.setFill("{color}")''')
        pre.append(f'''cir.setWidth({width})''')
        pre.append(f'''cir.draw(window)''')
        out.append(pre)
        coords = []
        del_temp_dots()
    else:
        return False

def line():
    global coords
    global window
    global out
    global outline_color

    if len(coords) == 2:
        cir = Line(Point(coords[0][0], coords[0][1]), Point(coords[1][0], coords[1][1]))
        cir.setOutline(outline_color)
        cir.setWidth(width)
        objects.append(cir)
        cir.draw(window)
        pre = []
        pre.append(f'''cir = Line(Point({coords[0][0]}, {coords[0][1]}),Point({coords[1][0]}, {coords[1][1]}))''')
        pre.append(f'''cir.setFill("{outline_color}")''')
        pre.append(f'''cir.setWidth({width})''')
        pre.append(f'''cir.draw(window)''')
        out.append(pre)
        coords = []
        del_temp_dots()
    else:
        return False

def pol():
    global coords
    global window
    global out
    global polygon
    global draw_polygon
    global color
    global width
    global outline_color

    cir = Polygon(polygon)
    cir.setOutline(outline_color)
    cir.setFill(color)
    cir.setWidth(width)
    objects.append(cir)
    cir.draw(window)
    draw_polygon = False

    pre = []
    pre.append(f'''cir = Polygon({polygon})''')
    pre.append(f'''cir.setOutline("{outline_color}")''')
    pre.append(f'''cir.setFill("{color}")''')
    pre.append(f'''cir.setWidth({width})''')
    pre.append(f'''cir.draw(window)''')
    out.append(pre)
    coords = []
    polygon = []
    del_temp_dots()

while True:
    mouse = window.checkMouse()
    if mouse != None:
        if mouse.getX() > 999 and (mouse.getY() >= 0 and mouse.getY() <= 100):
            try:
                color_new = picture.getPixel(round(mouse.getX()-1000),round(mouse.getY()))
                if sw_color:
                    color = color_rgb(color_new[0], color_new[1], color_new[2])
                else:
                    outline_color = color_rgb(color_new[0], color_new[1], color_new[2])
                draw_menu()
                continue
            except:
                print("ERROR GET COLOR FROM PALYTRA")
                continue


        if not draw_en[3]:
            coords.append([round(mouse.getX()), round(mouse.getY())])
        else:
            polygon.append(mouse)

        cir = Circle(mouse, 4)
        temp_dots.append(cir)
        cir.draw(window)

        try:


            if draw_en[0] == True:
                oval()
            elif draw_en[1] == True:
                rect()
            elif draw_en[2] == True:
                line()
        except:
            color = ""
            outline_color = "black"


    if back_en == True:
        if len(objects) != 0:
            objects[-1].undraw()
            back_en = False
            objects.pop(-1)
            print('''======================delete=================''')
            out.pop(-1)
        else:
            back_en = False

        coords = []

    if update_menu:
        draw_menu()
        update_menu = False

    if draw_polygon == True:
        pol()

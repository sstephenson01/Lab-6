# Sarah Stephenson and Rosemary Hoffman

import turtle
riley = turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)

def mood_star(mood):
    if mood == "happy":
        draw_star("yellow")
    elif mood=="sad":
            draw_star("blue")
    elif mood=="sleepy":
            draw_star("pink")
    else:
        draw_star("red")

mood_star("happy")

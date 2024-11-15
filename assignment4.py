# Assignment 4: Turtle Graphics Save the World
#Kenny Nguyen
#Oct 30th, 2024

#theme: 8
# Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all

#ideas: bar graph representing economic growth, arrow line representing stock growth and a giant infinity sign signifying sustainable growth and green background
import turtle
import random
#various turtles
screen = turtle.Screen()

infinity=turtle.Turtle()
t = turtle.Turtle()
line_turtle = turtle.Turtle()
name = turtle.Turtle()

infinity.speed(0)
name.speed(0)
t.speed(0)
line_turtle.speed(0)

spacing = 10

t.penup()
t.goto(-410,-400)
t.pendown()


def get_random_color_tuple():
    return tuple(random.randint(0, 255) for _ in range(3))


def get_random_color_name():
    colors = ['lawngreen',"SpringGreen2","OliveDrab1","LightGreen"]
    return random.choice(colors)

def draw_buildings(width,amount): 
    h = 10
    maxheight = 0
    counter = 0
    # Draw axes
    while counter <= 20:
        
        h = h + (h*0.5)
        if h >= 150:
            h = h - ((h/2) *0.5)
        t.begin_fill()
        screen.colormode(255)
        t.fillcolor(get_random_color_tuple())
        for i in range(2):
            t.left(90)
            t.forward(h)
            t.left(90)
            t.forward(width)   
        t.end_fill()
        maxheight = h
            
        t.penup()
        t.forward(width)
        t.pendown()
        counter+=1
        if counter == 20:
            break
    
    screen.colormode(1)
    t.begin_fill()
    t.fillcolor(str(get_random_color_name()))
    for i in range(2):
        t.left(90)
        t.forward(maxheight+50)
        t.left(90)
        t.forward(width)   
    t.end_fill()  
    t.hideturtle()

def draw_graph(width,amount):
        # Setup turtle
    line_turtle = turtle.Turtle()
    line_turtle.pencolor(get_random_color_name())
    line_turtle.penup()
    line_turtle.hideturtle()

    # Parameters
    initial_height = 20  

    # Generate and plot heights
    line_turtle.dot(5,get_random_color_name())
    line_turtle.hideturtle()
    
    line_turtle.goto(-450+40,-370)
    line_turtle.pendown()
    

    h = initial_height
    for i in range(1, amount+1):
        h = h + (h * 0.5)  # Increase by 50%
        if h >= 150:  # Apply cap
            h = h - ((h / 2) * 0.5)
        
        # Move turtle to the next position and draw the line
        line_turtle.goto((i*width)-450, h-400)
        
        line_turtle.dot(5, get_random_color_name())
        line_turtle.pendown()
        line_turtle.hideturtle()
    line_turtle.left(60)

#this function was created with help from online sources on the dimensions of an infinity sign
#Source: https://www.youtube.com/watch?v=0C6p5wQ5SwQ 
def draw_infinity():
    infinity.pencolor(get_random_color_name())
    infinity.penup()
    infinity.goto(-100,200)
    infinity.right(45)
    infinity.pendown()

    for i in range(150):
        infinity.circle(30)
        if 7 < i < 62:
            infinity.left(5)
        if 80 < i < 133:
            infinity.right(5)
        if i < 80:
            infinity.forward(10)
        else:
            infinity.forward(5)
    

def draw_name():
    name.pencolor("Red")
    name.penup()
    name.goto(-620,-380)
    name.pendown()
    name.left(90)
    name.forward(60)
    name.right(180)
    name.forward(30)
    name.left(90+45)
    name.forward(40)
    name.right(180)
    name.forward(40)
    name.left(90)
    name.forward(40)
    name.left(45)
    name.penup()

    name.goto(-580,-380)
    name.pendown()
    name.left(90)
    name.forward(60)
    name.right(90)
    name.forward(25)
    name.left(180)
    name.forward(25)
    name.left(90)
    name.forward(30)
    name.left(90)
    name.forward(25)
    name.right(180)
    name.forward(25)
    name.left(90)
    name.forward(30)
    name.left(90)
    name.forward(25)
    name.penup()
    name.goto(-540,-380)
    
    name.pendown()
    name.left(90)
    name.forward(60)
    name.right(90+60)
    name.forward(70)
    name.left(90+60)
    name.forward(60)
    name.right(180)
    name.forward(60)
    name.left(90)
    name.penup()

    name.goto(-470,-380)
    name.pendown()
    name.left(90)
    name.forward(60)
    name.right(180)
    name.forward(30)
    name.right(90)
    name.forward(30)
    name.right(90)
    name.forward(30)
    name.hideturtle()


def main():
    screen.bgcolor("black")
    draw_name()
    draw_buildings(40,20)
    t.penup()
    t.goto(-410,-400)
    t.pendown()
    draw_graph(40,20)
    draw_infinity()
   
main()
turtle.Screen().exitonclick()

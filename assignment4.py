# Assignment 4: Turtle Graphics Save the World
#Kenny Nguyen
#Oct 30th, 2024

#theme: 8
# Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all

#ideas: bar graph representing economic growth, arrow line representing stock growth and a giant infinity sign signifying sustainable growth and green background
import turtle
import math
import random

t = turtle.Turtle()
axis_turtle = turtle.Turtle()
line_turtle = turtle.Turtle()
t.speed(0)
axis_turtle.speed(0)

spacing = 10
t.penup()
t.goto(-410,-400)
t.pendown()



def get_random_color_tuple():
    return tuple(random.randint(0, 255) for _ in range(3))

def get_random_color_name():
    colors = ['aquamarine',"blue","purple","red"]
    return random.choice(colors)

def draw_buildings(width,height,start,end,amount): 
    last_building = 0
    # Calculating the scale


    for i in range(amount):
        height = random.randint(start,end)
        maxheight = end 
        t.begin_fill()
        t.fillcolor(str(get_random_color_name()))
        for i in range(2):
            t.left(90)
            t.forward(height)
            t.left(90)
            t.forward(width)   
        t.end_fill()
            
        t.penup()
        t.forward(width )
        t.pendown()

    t.begin_fill()
    t.fillcolor(str(get_random_color_name()))
    for i in range(2):
        t.left(90)
        t.forward(maxheight+100)
        t.left(90)
        t.forward(width)   
    t.end_fill()  


    

    stock_prices = [100, 105, 102, 110, 108, 115, 113, 120, 118, 300]

def draw_graph(width,start,end,amount):
    # Calculating the scale
    max_price = end
    min_price = start
    # Plot starting position
    start_x = -410
    start_y = -400

    plot_height = 410
    plot_width = width* amount

    # Draw axes
    axis_turtle.penup()
    axis_turtle.goto(start_x, start_y)
    axis_turtle.pendown()
    axis_turtle.forward(width* amount)
    axis_turtle.penup()
    axis_turtle.goto(start_x, start_y)
    axis_turtle.left(90)
    axis_turtle.pendown()
    axis_turtle.forward(max_price)
    

    # Plot the stock line
    
    point_spacing = plot_width / (amount - 1)

    for i in range(amount):
        # Generate a random stock price
        price = random.randint(start,end)
        
        # Map stock price to the plot height
        x = start_x + i * point_spacing
        y = start_y + (price - min_price) / (max_price - min_price) * plot_height
        
        # Move to the first point without drawing
        if i == 0:
            line_turtle.goto(x, y)
            line_turtle.pendown()
        else:
            # Draw line to the next point
            line_turtle.goto(x, y)


draw_buildings(40,100,1,250,20)
draw_graph(40,1,250,20)


turtle.Screen().exitonclick()

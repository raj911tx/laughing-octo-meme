import turtle

my_turtle = turtle.Turtle()
my_window = turtle.Screen()

points=[[-100,-50],[0,100],[100,-50]]

def draw_triangle(points,my_turtle,color):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1])
    my_turtle.goto(points[2])
    my_turtle.goto(points[0])
    my_turtle.end_fill()

def mid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski_triangle(points,degree,my_turtle):
    colors=['red','violet','pink','green','yellow','orange','blue','magenta']
    draw_triangle(points,my_turtle,colors[degree])
    if degree>0:
        sierpinski_triangle((points[0],mid(points[0],points[1]),mid(points[0],points[2])),degree-1,my_turtle)
        sierpinski_triangle((points[1],mid(points[0],points[1]),mid(points[1],points[2])),degree-1,my_turtle)
        sierpinski_triangle((points[2],mid(points[2],points[1]),mid(points[0],points[2])),degree-1,my_turtle)

sierpinski_triangle(points,4,my_turtle)
my_window.exitonclick()

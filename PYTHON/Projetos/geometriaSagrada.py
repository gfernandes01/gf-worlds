import turtle

color = ('yellow', 'red', 'green', 'orange', 'blue', 'white')

form = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
form.speed(30)

for i in range(150):
	form.color(color[i%6])
	form.forward(i*4)
	form.left(150)
	form.width(2)
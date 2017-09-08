import turtle, random

test = turtle.Turtle()
wn = turtle.Screen()
test.speed(100)
#Stets the speed to 100

colors = ["red", "green", "orange", "pink", "yellow", "blue", "white"]
colors2 = ["white", "yellow", "blue", "purple"]
#Array/List for all colars
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numbers2 = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.19]
#numbers3 = [50, 100, 150, 200, 250, 300, 350]
wn.bgcolor("black")

#test.goto(0, -100)
#sets pen to position x0 ,y-100
for i in range(500):
	test.width(random.choice(numbers))
	#Width of the Pen
	
	#test.color(colors[4])
	test.color(random.choice(colors2))
	#random pen color with array colors
	test.penup()
	#Lift the Pen
	test.forward(i * random.choice(numbers2))
	test.pendown()
	#put pen down
	test.forward(1)
	#Wrights 1 px forward 
	test.right(271)
	#turns pen 271° right (also left for max of 360° (full turn))
	
ts = turtle.getscreen()
#Save screnshot as ts
#turtle.bgpic("text.gif")


#turtle.exitonclick()
ts.getcanvas().postscript(file="new.eps")
#Saven the ts as Picture in eps (eps can open with Photoshop)
turtle.done()
#Waits for closing manualy

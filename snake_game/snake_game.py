import turtle
import time
import random

delay = 0.1

score= 0
high_score=0
turtle.colormode(255)
wn=turtle.Screen()
wn.title("Snake Game by @AliAbbas")
wn.bgcolor("black")
wn.setup(width=600, height=600)

#Turn off animation from acreen 
wn.tracer(0)

#Snake configuration
head= turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'


#snake food configuration
food= turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color((234, 18, 184))
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Score: 0  High Score: 0", align="center", font=("Cairo", 24, "normal"))

#snake body segments
segments= []

#all functions
def go_up():
	head.direction = "up"
def go_down():
	head.direction = "down"
def go_left():
	head.direction = "left"
def go_right():
	head.direction = "right"


def move():
	if head.direction == "up":
		y=head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y=head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x=head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x=head.xcor()
		head.setx(x + 20)
#main game loop to check events

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
	wn.update()
	if head.xcor() > 290:
		head.setx(-290)
	elif head.xcor() < -290:
		head.setx(290)
	elif head.ycor() > 290:
		head.sety(-290)
	elif head.ycor() < -290:
		head.sety(290)
    #collision check for border
	#check if snake collides with food
	if head.distance(food) < 20:
		x=random.randint(-290,290)
		y=random.randint(-290,290)
		food.goto(x,y)
		new_segment=turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("white")
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Cairo", 24, "normal"))

	for index in range(len(segments)-1, 0, -1):
		x= segments[index-1].xcor()
		y= segments[index-1].ycor()
		segments[index].goto(x,y)
	
	if len(segments) > 0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)

	move()

	#check for snake collision with itself
    #optional conditon to avoid collison fail on reverse direction
	#(segments[segment].xcor() >= segments[segment-1].xcor() or segments[segment].ycor() >= segments[segment-1].ycor())
	for segment in segments:
		if segment.distance(head) < 20 :
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()
			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Cairo", 24, "normal"))
	time.sleep(delay)
    
wn.mainloop()
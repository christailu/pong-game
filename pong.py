import turtle

# window se refaire a ecran
window = turtle.Screen() #S doit etre en majusccule
window.title("Pong game by Christa")
window.bgcolor("white") # bg = background color
window.setup(width = 800, height = 600)
window.tracer(0) # stop the window from updating

#score 
score_A =0
score_B =0
#premeiere raquette
pad_A = turtle.Turtle()
pad_A.speed(0)
pad_A.shape("square")
pad_A.color("black")
pad_A.shapesize(stretch_wid= 5, stretch_len= 1)
pad_A.penup()
pad_A.goto(-350, 0)


# deuxieume raquette

pad_B = turtle.Turtle()
pad_B.speed(0)
pad_B.shape("square")
pad_B.color("black")
pad_B.shapesize(stretch_wid= 5, stretch_len= 1)
pad_B.penup()
pad_B.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.goto(0, 260)
pen.write("Joueur 1: 0 Joueur 2: 0", align = "center", font=("courier", 24, "normal"))

#Function 
def pad_A_up():
    y =pad_A.ycor() #ycol will return the value of the y cordinate
    y += 20 #add 20 pixel  to the pad
    pad_A.sety(y)
    
def pad_A_down():
    y =pad_A.ycor() #ycol will return the value of the y cordinate
    y -= 20 #add 20 pixel  to the pad
    pad_A.sety(y)    
    
def pad_B_up():
    y =pad_B.ycor() #ycol will return the value of the y cordinate
    y += 20 #add 20 pixel  to the pad
    pad_B.sety(y)
    
def pad_B_down():
    y =pad_B.ycor() #ycol will return the value of the y cordinate
    y -= 20 #add 20 pixel  to the pad
    pad_B.sety(y)     
    
# keyboard biding
window.listen() # listen for keyboard input
window.onkeypress(pad_A_up, "w") #if the user press w    
window.onkeypress(pad_A_down, "s") 
window.onkeypress(pad_B_up, "Up")
window.onkeypress(pad_B_down, "Down")

#Main game loop
while True:
    window.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_A += 1 
        pen.clear()
        pen.write("Joueur 1: {} Joueur 2: {}".format(score_A, score_B), align = "center", font=("sans serif", 24, "normal"))           
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_B += 1 
        pen.clear()

              
    # collision avec la ball
    if ball.xcor() > 340 and (ball.ycor() < pad_B.ycor() + 40 and ball.ycor() > pad_B.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1          
        
    if ball.xcor() < -340 and (ball.ycor() < pad_A.ycor() + 40 and ball.ycor() > pad_A.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1          

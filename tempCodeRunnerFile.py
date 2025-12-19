from turtle import Turtle,Screen
import random
window=Screen()
window.bgcolor('black')
window.setup(width=600,height=600)
window.title('النسخه المعدله من اللعبه')
user_choice=window.textinput('Welcome to in my world','enter the win color turtle')

colors=["red",'green','blue3']
random.shuffle(colors)
y_position=(-70,0,70)
all_turtle=[]
winner=[]
 
for x in range(3):
    new_turtle=Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.goto(x=-280,y=y_position[x])
    new_turtle.color(colors[x])
    all_turtle.append(new_turtle)
 
def race():
   race_on=True
   while race_on:
     for tur in all_turtle:
          if tur.xcor() >=280:
               race_on=False
               winner.append(tur)

          else:
               tur.forward(random.randint(1,5))

def how_win():
     tom=Turtle()
     tom.hideturtle()
     tom.color('white')
     tom.penup()
     tom.goto(0,0)
     tom.pendown()
     
     if user_choice==winner[0]:
          window.bgcolor('lightgreen')
          tom.write('you win ',align='center',font=('arial',38,'normal'))
     else:
          window.bgcolor('gray')
          tom.write(' you loss',align='center',font=('arial',38,'normal'))

race()
how_win()

window.exitonclick()
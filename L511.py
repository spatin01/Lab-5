#Names: Samantha Patin and Elise Ward

import turtle

riley=turtle.Turtle()
riley.width(5)
riley.speed(2)

def draw_star(mood):
    for side in range(5):
        if mood=="happy":
            riley.color("pink")
        elif mood=="sad":
            riley.color("blue")
        elif mood=="sleepy":
            riley.color("green")
        elif mood=="angry":
            riley.color("red")
        riley.forward(100)
        riley.right(144)
        
user_mood = input("Enter mood (happy, sad, angry, sleepy):")

draw_star(user_mood)

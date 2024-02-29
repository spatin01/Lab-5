#Names: Samantha Patin and Elise Ward

#A: If Statements

x=2
if x<3:
    print("Small")
x=5
if x<3:
    print("Small")

score=8
#A score on a 10 point quiz
if score>6:
    print("Nice work!")

#prediction: function will print:
    #3 is divisible by 3.
    #6 is divisible by 3.
    #9 is divisible by 3.
    #12 is divisible by 3.
    #15 is divisible by 3.

for i in range (1, 16):
    if i%3==0:
        print(i, "is divisible by 3.")

#Adapt:

def even_odd(integer):
    if integer%2==0:
        print("Even")

even_odd(2002)
even_odd(17)

#B: elif and else Statements

x=2
if x<3:
    print("Small")
else:
    print("Large")

x=5
if x<3:
    print("Small")
else:
    print("Large")

score=8
if score<6:
    print("Needs improvement")
elif score<9:
    print("Nice work!")
else:
    print("Excellent!")

#Predict: function will print:
    #-2 is negative, -1 is negative
    #0 is zero
    #1 is positive, 2 is positive

for i in range(-2,3):
    if i<0:
        print(i, "is negative.")
    elif i==0:
        print(i, "is zero.")
    else:
        print(i, "is positive.")
        
#Adapt:
    
def even_odd(integer):
    if integer%2==0:
        print("Even")
    else:
        print("Odd")

even_odd(2002)
even_odd(17)

#C: Booleans

print(3<4)
print(4<2)
print(True)

if True:
    print("This text will always appear.")
if False:
    print("This text will not appear.")
    
#Predict: type(False) --> booleane, print(3==5)--> False

print(type(False))
print(3==5)

#Adapt:

def number10 (x):
    print(x>10)

number10(22)
number10(7)



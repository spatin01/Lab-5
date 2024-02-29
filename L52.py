#Names: Samantha Patin and Elise Ward

#defined perfect number function
def perfect (y):
    summ=0
    for x in range(1, y):
        if (y%x==0):
            summ=summ+x


    if summ==y:
         print(summ==y)
    elif summ!=y:
        print(summ==y)
            
#test function
perfect(6)
perfect(15)
perfect(28)

#user input number
num = input("Enter a number:")
num = int(num)

#check user input for perfect
perfect(num)

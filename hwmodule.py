from tkinter import Y


square_ft = []

def mult ():
    l = int(input("What is length of your house in feet?"))
    w = int(input("What is the width of your house in feet?"))
    sq_foot = l * w 
    square_ft.append(sq_foot)
    print(square_ft)

mult()


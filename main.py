from tkinter import *
import numpy as numpy
from random import *
#the tkinter frame setup
root = Tk()
root.geometry('1000x1000')
root.title("Conway's Game of Life")
canvas = Canvas(root,height = 500, width = 1000, bg = 'black')
for i in range(100,1000,100):
    canvas.create_line(i,0,i,500,fill='white')
for j in range(50,500,50):
    canvas.create_line(0,j,1000,j,fill='white') 
#this function creates the new array that results from the implementation of Life's rules.
def nextgen(arr):
    y = numpy.zeros((10,10))
    for i in range(0,10):
        for j in range(0,10):
            c = check(arr,i,j)
            if c == 3:
                y[i][j] = 1
            elif c == 2 and arr[i][j] == 1:
                y[i][j] = 1
            elif c == 2 and arr[i][j] == 0:
                y[i][j] = 0
            elif c > 3:
                y[i][j] = 0
            elif c < 2:
                y[i][j] = 0
    return y

#This function is for checking the neighbors and counting how many are alive.
def check(arr,i,j):
    count = 0
    for i2 in range(i-1,i+2):
            for j2 in range(j-1,j+2):
                try:
                    if not ((i2==i) and (j2==j)):
                        if arr[i2][j2] == 1:
                            count = count + 1
                except:
                    pass
    return count

#This function creates a setup to represent the original population
def start():
    global a
    canvas.delete('box')
    x = numpy.zeros((10,10))
    for w in range(randint(1,50)):
        x[randint(0,9)][randint(0,9)] = 1
    for i in range(0,9):
        for j in range(0,9):
            if x[i][j] == 1:
                canvas.create_rectangle(i*100,j*50,i*100 + 100,j*50+50,fill='red', tag='box')
    a = x
    return x
def make_nextgen():
    global a
    y = numpy.zeros((10,10))
    canvas.delete('box')
    y = nextgen(a)
    for i in range(0,9):
        for j in range(0,9):
            if y[i][j] == 1:
                canvas.create_rectangle(i*100,j*50,i*100 + 100,j*50+50,fill='red', tag='box')
    a = y
    return a

def common():
    canvas.delete('box')
    global a
    x = numpy.zeros((10,10))
    x[6][4] = 1
    x[6][5] = 1
    x[6][6] = 1
    for i in range(0,9):
        for j in range(0,9):
            if x[i][j] == 1:
                canvas.create_rectangle(i*100,j*50,i*100 + 100,j*50+50,fill='red', tag='box')
    a = x
    return x
    
    
#tkinter frame closing code/ button creation
b1 = Button(root,text = 'Start', command = start)
b2 = Button(root,text = 'Next Generation', command = make_nextgen)
b3 = Button(root,text='The Common Pattern', command=common)
b1.place(x=250,y=600,width=200,height=30)
b2.place(x=500,y=600,width=200,height=30)
b3.place(x=300,y=650,width=200,height=30)
canvas.pack()
root.mainloop()
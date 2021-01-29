from turtle import*
from random import choice
import time

bgcolor("black")
color("grey")
centerx = -200
centery = 200
col = 20
row = 20
pix = 20
x = 0
y = 0
tracer(0)
penup()
goto(centerx, centery)
on = Turtle()
matrix = [[0] * col for i in range(row)]




def drawGrid(col, row, pix):
    for step in range(col + 1):
        right(90)

        for num in range(row):
            pendown()
            forward(pix)
        

        penup()
        backward(pix * row)
        left(90)
        forward(pix)

    goto(centerx, centery)

    for step in range(row + 1):

        for num in range(col):
            pendown()
            forward(pix)

        penup()
        backward(pix * col)
        right(90)
        forward(pix)
        left(90)

    goto(centerx, centery)


def fillSquare(x, y, pix):

    on.penup()
    on.color("pink")
    on.goto(centerx, centery)
    on.fillcolor("white")
    on.goto(centerx + x * pix, centery - y * pix)
    on.begin_fill()
    for side in range(4):
        on.forward(pix)
        on.right(90)
    on.end_fill()
    on.goto(centerx, centery)


def createMatrix(col, row):
    
    for i in range(col):
        for j in range(row):
            matrix[i][j] = choice([0, 0, 0, 1])
            if matrix[i][j] == 1:
                fillSquare(i, j, pix)
    


def compute(col, row, matrix):
    nextMatrix = [[0] * col for i in range(row)]
    for i in range(col):
        for j in range(row):
            state = matrix[i][j]
            if (i == 0 or i == col - 1 or j == 0 or j == row - 1):
                nextMatrix[i][j] = state
                continue
                print("not bro\n--------------")
            
            total = countNearby(i, j, matrix) 
            #print("this the total")
            #print(total)
            #print("this the state")
            #print(state)
            #print(i,j,col,row)

            if state == 0 and total == 3:
                nextMatrix[i][j] = 1
                fillSquare(i, j, pix)
                #print("bro")

            elif state == 1 and (total == 3 or total == 2):
                nextMatrix[i][j] = 1
                fillSquare(i, j, pix)
                #print("bro2")

            else:
                nextMatrix[i][j] = 0
                #print("bro3")
    #print(matrix) 
    #print(nextMatrix)
    matrix = nextMatrix
    #print(matrix)
    return matrix


def countNearby(xx, yy, matrix):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            sum += matrix[xx + i][yy + j]
    sum -= matrix[xx][yy]
    return sum


drawGrid(col, row, pix)
createMatrix(col, row)
update()
while True:
        #time.sleep(0.1)
        on.clear()
        matrix = compute(col, row, matrix)
        
        #print(count)
        
        update()

update()
                                
                                                
 
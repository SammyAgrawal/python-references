import math
from graphics import *

input = raw_input

def JuliaSet(m, n, s, win):
    print("Press space to zoom out, click a point to zoom in, or spam q to exit")
    for a in range(0,size):
        for b in range(0,size):
            color = "white"
            x0 = m + (s*a)/(size)
            y0 = n - (s*b)/(size)
            for i in range(1,20):
                x1 = x0*x0 - y0*y0 + cx
                y1 = 2*x0*y0 + cy
                if x1*x1 + y1*y1 <= 10:
                    x0 = x1
                    y0 = y1
                else:
                    color = color_rgb(12*i, 0, 12*i)
                    break
            if color:
                win.plot(a, b, color)
    update()
    while True:
        clickpoint = win.checkMouse()
        key = win.checkKey()
        if clickpoint:
            adjustpoint = [m + clickpoint.getX()/size*s, n - clickpoint.getY()/size*s]
            print adjustpoint
            m = adjustpoint[0] - s/4
            n = adjustpoint[1] + s/4
            JuliaSet(adjustpoint[0] - s/4, adjustpoint[1] + s/4, s/2, win)
        if key == "space":
            JuliaSet(m-s/2,n+s/2,2*s,win)
        if key == "q":
            break

def MandelbrotSet(m, n, s, win):
    print("Press space to zoom out, click a point to zoom in, or spam q to exit")
    for a in range(0,size):
        cx = m + (s*a)/(size)
        for b in range(0,size):
            cy = n - (s*b)/(size)
            color = "black"
            x0 = 0
            y0 = 0
            for i in range(1,20):
                x1 = x0*x0 - y0*y0 + cx
                y1 = 2*x0*y0 + cy
                if x1*x1 + y1*y1 <= 4:
                    x0 = x1
                    y0 = y1
                else:
                    color = color_rgb(255-12*i, 12*i, 12*i)
                    break
            if color:
                win.plot(a, b, color)
    update()
    while True:
        clickpoint = win.checkMouse()
        key = win.checkKey()
        if clickpoint:
            adjustpoint = [m + clickpoint.getX()/size*s, n - clickpoint.getY()/size*s]
            print adjustpoint
            m = adjustpoint[0] - s/4
            n = adjustpoint[1] + s/4
            MandelbrotSet(adjustpoint[0] - s/4, adjustpoint[1] + s/4, s/2, win)
        if key == "space":
            MandelbrotSet(m-s/2,n+s/2,2*s,win)
        if key == "q":
            break

a = "y"
while a == "y":
    size = int(input("What size? "))
    m = -2
    n = 2
    s = 4.0
    #m = float(input("Left X? (-2 is regular) "))
    #n = float(input("Top Y? (2 is regular) "))
    #s = float(input("Zoom? (less is more, 4.0 is regular) "))
    JorM = input("Julia or Mandy? (or all but prepare yourself) ")
    if JorM == "Julia":
        cx = float(input("Real part of complex constant: "))
        cy = float(input("Imaginary part of complex constant: "))
        win = GraphWin("Complex Plane", size, size, autoflush=False)
        win.setCoords(0,size,size,0)
        win.setBackground("black")
        JuliaSet(m, n, s, win)
        win.close()
    if JorM == "Mandy":
        win = GraphWin("Complex Plane", size, size, autoflush=False)
        win.setCoords(0,size,size,0)
        win.setBackground("black")
        MandelbrotSet(m, n, s, win)
        win.close()
    if JorM == "all":
        cx = -1
        while cx <= 1:
            cy = 1
            while cy >= -1:
                win = GraphWin("z^2 + %0.2f + %0.2fi"%(cx,cy), size, size, autoflush=False)
                win.setCoords(0,size,size,0)
                win.setBackground("black")
                for a in range(0,size):
                    for b in range(0,size):
                        color = "white"
                        x0 = m + (s*a)/(size)
                        y0 = n - (s*b)/(size)
                        for i in range(1,20):
                            x1 = x0*x0 - y0*y0 + cx
                            y1 = 2*x0*y0 + cy
                            if x1*x1 + y1*y1 <= 4:
                                x0 = x1
                                y0 = y1
                            else:
                                color = color_rgb(12*i, 0, 12*i)
                                break
                        if color:
                            win.plot(a, b, color)
                cy = cy - 0.5
            cx = cx + 0.5
        win = GraphWin("Complex Plane", size, size, autoflush=False)
        win.setCoords(0,size,size,0)
        win.setBackground("black")
        MandelbrotSet(-2,2,4.0,win)
    a = input("Do you want to play again? (y or n) ")

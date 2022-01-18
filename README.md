# IP-Assignment-3
In this project I have made an interactive Python program to apply transformations to an object and plot it using matplotlib. 
In the code I have used the concept of Object Oriented Programming in Python, and have used the libraries under MATPLOT LIB to plot and display the Graphs created.
The code is for 2 shapes: Polygon & Circle.
The output is menu based and in the code, there are 5 functionalities.
Functionalities in the code are:
1) __init__(): Initializations have to be done here.
2) translate(): Takes in 2 arguments dx and dy (dy is optional). Here, dx is a number which implies how much to 
                translate with along x-axis and similarly, dy along y-axis.
3) rotate(): Takes in 3 arguments deg (Φ), rx, ry (rx and ry are optional arguments which implies coordinates of arbitrary point from where rotation will take place).
4) scale(): Takes in 2 arguments, sx and sy in case of a polygon and 1 argument s in case of a circle.
5) plot(): Plot the initial and the transformed shape using matplotlib library. Plot the before and after transformation plots.

Each transformation will be performed on the shape obtained as a result of all the previous transformations in a cumulative manner. 
The first transformation will be performed on the original state of the shape as provided by the user.

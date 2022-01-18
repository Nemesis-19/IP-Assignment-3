import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    # '''
    # DO NOT MODIFY THIS CLASS

    # DO NOT ADD ANY NEW METHODS TO THIS CLASS
    # '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        # '''
        # Polygon and Circle class should use this function to calculate the translation
        # '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        # '''
        # Polygon and Circle class should use this function to calculate the scaling
        # '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        # '''
        # Polygon and Circle class should use this function to calculate the rotation
        # '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        # '''
        # Polygon and Circle class should use this function while plotting
        # x_dim and y_dim should be such that both the figures are visible inside the plot
        # '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    # '''
    # Object of class Polygon should be created when shape type is 'polygon'
    # '''
    def __init__(self, A):
        # '''
        # Initializations here
        # '''
        # pass

        self.A = A
        
        side = len(A)

        self.x_in = [] # making empty lists for reserved for further use

        self.y_in = []

        self.lst_x_in = []

        self.lst_y_in = []

        for i in range(side) :  # iterating list

            (self.x_in).append(float(A[i][0]))

        for i in range(side) :

            (self.y_in).append(float(A[i][1]))

        self.side = side
    
    def translate(self, dx, dy):
        # '''
        # Function to translate the polygon
    
        # This function takes 2 arguments: dx and dy
    
        # This function returns the final coordinates
        # '''
        # pass

        Shape.translate(self, dx, dy)  # making array

        self.lst_x_in = self.x_in

        self.lst_y_in = self.y_in

        self.x_in = []

        self.y_in = []

        # using array made above to translate

        for i in range(len(self.A)) :

            x_fin = self.lst_x_in[i] * self.T_t[0][0] + self.lst_y_in[i] * self.T_t[0][1] + 1 * self.T_t[0][2]

            (self.x_in).append(x_fin.round(2))

        for i in range(len(self.A)) :

            y_fin = self.lst_x_in[i] * self.T_t[1][0] + self.lst_y_in[i] * self.T_t[1][1] + 1 * self.T_t[1][2]

            (self.y_in).append(y_fin.round(2))

        return self.x_in, self.y_in  # returning final solution
    
    def scale(self, sx, sy):
        # '''
        # Function to scale the polygon
    
        # This function takes 2 arguments: sx and sx
    
        # This function returns the final coordinates
        # '''
        # pass
 
        Shape.scale(self, sx, sy)  # making array

        self.lst_x_in = self.x_in

        self.lst_y_in = self.y_in

        self.x_in = []

        self.y_in = []

        mean_init_x = 0

        mean_init_y = 0

        mean_fin_x = 0

        mean_fin_y = 0

        # finding initial mean

        for i in range(len(self.lst_x_in)) :

            mean_init_x = mean_init_x + self.lst_x_in[i]

        mean_init_x = mean_init_x / self.side

        for i in range(len(self.lst_y_in)) :

            mean_init_y = mean_init_y + self.lst_y_in[i]

        mean_init_y = mean_init_y / self.side

        # using array to scale

        for i in range(self.side) :

            x_fin = self.lst_x_in[i] * self.T_s[0][0] + self.lst_y_in[i] * self.T_s[0][1] + 1 * self.T_s[0][2]

            (self.x_in).append(x_fin)

        for i in range(self.side) :

            y_fin = self.lst_x_in[i] * self.T_s[1][0] + self.lst_y_in[i] * self.T_s[1][1] + 1 * self.T_s[1][2]

            (self.y_in).append(y_fin)

        # finding final mean

        for i in range(len(self.x_in)) :

            mean_fin_x = mean_fin_x + self.x_in[i]

        mean_fin_x = mean_fin_x / self.side

        for i in range(len(self.y_in)) :

            mean_fin_y = mean_fin_y + self.y_in[i]

        mean_fin_y = mean_fin_y / self.side

        # final adjustment

        for i in range(len(self.x_in)) :

            self.x_in[i] = (mean_init_x - mean_fin_x + self.x_in[i]).round(2)

        for i in range(len(self.y_in)) :

            self.y_in[i] = (mean_init_y - mean_fin_y + self.y_in[i]).round(2)

        return self.x_in, self.y_in

    def rotate(self, deg, rx = 0, ry = 0):
        # '''
        # Function to rotate the polygon
    
        # This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        # This function returns the final coordinates
        # '''
        # pass

        Shape.rotate(self, deg) # making array

        self.lst_x_in = self.x_in

        self.lst_y_in = self.y_in

        lst_x = self.x_in

        lst_y = self.y_in

        # translating 1st

        lst_x, lst_y = self.translate(-rx, -ry)

        self.x_in = []

        self.y_in = []

        # ussing array for the multiplication

        for i in range(self.side) :

            x_fin = lst_x[i] * self.T_r[0][0] + lst_y[i] * self.T_r[0][1] + 1 * self.T_r[0][2]

            (self.x_in).append(x_fin.round(2))

        for i in range(self.side) :

            y_fin = lst_x[i] * self.T_r[1][0] + lst_y[i] * self.T_r[1][1] + 1 * self.T_r[1][2]

            (self.y_in).append(y_fin.round(2))

        # again translating

        self.x_in, self.y_in = self.translate(rx, ry)

        return self.x_in, self.y_in

    def plot(self):
        # '''
        # Function to plot the polygon
    
        # This function should plot both the initial and the transformed polygon
    
        # This function should use the parent's class plot method as well
    
        # This function does not take any input
    
        # This function does not return anything
        # '''
        # pass

        # checking if it is 1st time plotting

        if self.lst_x_in == [] and self.lst_y_in == [] :

            lst_x = self.x_in

            lst_x.append(self.x_in[0])

            lst_y = self.y_in

            lst_y.append(self.y_in[0])

            plt.plot(lst_x, lst_y)

            # Shape.plot(self, max(lst_x), max(lst_y))

            lst_x_fin = []

            lst_y_fin = []

            # making values absolute so as to avoid mistakes

            for i in range(len(lst_x)) :

                lst_x_fin.append(abs(lst_x[i]))

            for i in range(len(lst_y)) :

                lst_y_fin.append(abs(lst_y[i]))

            Shape.plot(self, max(lst_x_fin), max(lst_y_fin))

        else :

            # printing previous graphs

            lst_x = self.lst_x_in

            lst_x.append(self.lst_x_in[0])

            lst_y = self.lst_y_in

            lst_y.append(self.lst_y_in[0])

            # printing final graphs

            lst_x_2 = self.x_in

            lst_x_2.append(self.x_in[0])

            lst_y_2 = self.y_in

            lst_y_2.append(self.y_in[0])

            lst_x_fin_i = []

            lst_y_fin_i = []

            lst_x_fin_f = []

            lst_y_fin_f = []

            # Shape.plot(self, max(max(self.lst_x_in), max(self.x_in)), max(max(self.lst_y_in), max(self.y_in)))

            for i in range(len(self.lst_x_in)) :

                lst_x_fin_i.append(abs(self.lst_x_in[i]))

            for i in range(len(self.lst_y_in)) :

                lst_y_fin_i.append(abs(self.lst_y_in[i]))

            for i in range(len(self.x_in)) :

                lst_x_fin_f.append(abs(self.x_in[i]))

            for i in range(len(self.y_in)) :

                lst_y_fin_f.append(abs(self.y_in[i]))

            plt.plot(lst_x, lst_y, linestyle = "dashed")

            plt.plot(lst_x_2, lst_y_2)

            Shape.plot(self, max(max(lst_x_fin_i), max(lst_x_fin_f)), max(max(lst_y_fin_i), max(lst_y_fin_f)))

class Circle(Shape):
    # '''
    # Object of class Circle should be created when shape type is 'circle'
    # '''
    def __init__(self, x=0, y=0, radius=5):
        # '''
        # Initializations here
        # '''
        # pass

        # initializing and making resevre variables for further use

        self.x_in = float(x)

        self.y_in = float(y)

        self.r_in = float(radius)

        self.x_i_in = self.x_in

        self.y_i_in = self.y_in
        
        self.r_i_in = self.r_in
    
    def translate(self, dx, dy):
        # '''
        # Function to translate the circle
    
        # This function takes 2 arguments: dx and dy (dy is optional).
    
        # This function returns the final coordinates and the radius
        # '''
        # pass

        Shape.translate(self, dx, dy) # making array

        self.x_i_in = self.x_in

        self.y_i_in = self.y_in
        
        self.r_i_in = self.r_in

        # using array for multiplication

        self.x_in = (self.x_i_in * self.T_t[0][0] + self.y_i_in * self.T_t[0][1] + 1 * self.T_t[0][2]).round(2)

        self.y_in = (self.x_i_in * self.T_t[1][0] + self.y_i_in * self.T_t[1][1] + 1 * self.T_t[1][2]).round(2)

        return self.x_in, self.y_in, self.r_in # returning final solution
        
    def scale(self, sx):
        # '''
        # Function to scale the circle
    
        # This function takes 1 argument: sx
    
        # This function returns the final coordinates and the radius
        # '''
        # pass

        # making array

        Shape.scale(self, sx, sx)
        
        self.r_i_in = self.r_in

        # using it for multiplication

        self.r_in = (self.r_i_in * self.T_s[0][0] + self.r_i_in * self.T_s[0][1] + 1 * self.T_s[0][2]).round(2)

        return self.x_in, self.y_in, self.r_in
    
    def rotate(self, deg, rx = 0, ry = 0):
        # '''
        # Function to rotate the circle
    
        # This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        # This function returns the final coordinates and the radius
        # '''
        # pass

        # making array

        Shape.rotate(self, deg)

        self.x_i_in = self.x_in

        self.y_i_in = self.y_in

        self.r_i_in = self.r_in

        x = self.x_i_in

        y = self.y_i_in

        r = self.r_i_in

        # translating

        self.x_i_in, self.y_i_in, self.r_i_in = self.translate(-rx, -ry)

        # using array for multiplication

        self.x_in = (self.x_i_in * self.T_r[0][0] + self.y_i_in * self.T_r[0][1] + 1 * self.T_r[0][2]).round(2)

        self.y_in = (self.x_i_in * self.T_r[1][0] + self.y_i_in * self.T_r[1][1] + 1 * self.T_r[1][2]).round(2)

        # translating again to get correct center

        self.x_in, self.y_in, self.r_in = self.translate(rx, ry)

        x = self.x_i_in

        y = self.y_i_in

        r = self.r_i_in

        return self.x_in, self.y_in, self.r_in # returning final solution
    
    def plot(self):
        # '''
        # Function to plot the circle
    
        # This function should plot both the initial and the transformed circle
    
        # This function should use the parent's class plot method as well
    
        # This function does not take any input
    
        # This function does not return anything
        # '''
        # pass

        # checking if plot is used 1st time or not

        if self.x_in == self.x_i_in and self.y_in == self.y_i_in and self.r_in == self.r_i_in :

            circle = plt.Circle((self.x_in,self.y_in), self.r_in, fill = False)

            plt.gca().add_patch(circle)

            plt.axis("scaled")

            # plotting graphs using absolute values

            Shape.plot(self, abs(self.x_in + self.r_in), abs(self.y_in + self.r_in))

        else :

            # plotting previous graph

            circle = plt.Circle((self.x_i_in,self.y_i_in), self.r_i_in, fill = False, linestyle = "dashed")

            plt.gca().add_patch(circle)

            plt.axis("scaled")

            # plotting final graph

            circle = plt.Circle((self.x_in,self.y_in), self.r_in, fill = False)

            plt.gca().add_patch(circle)

            plt.axis("scaled")

            # Shape.plot(self, max(abs(self.x_in) + abs(self.r_in), abs(self.x_i_in) + abs(self.r_i_in)), max((abs(self.y_in) + abs(self.r_in)), (abs(self.y_i_in) + abs(self.r_i_in))))

            # Shape.plot(self, max((abs(self.x_i_in) + abs(self.r_i_in)), abs(self.x_in) + abs(self.r_in)), max(abs(self.y_i_in) + abs(self.r_i_in), abs(self.y_in) + abs(self.r_in)))

            # Shape.plot(self,max((abs(self.t_x)+abs(self.t_r)),abs(self.x)+abs(self.r)),max(abs(self.t_y)+abs(self.t_r),abs(self.y)+abs(self.r)))

            Shape.plot(self, max(abs(self.x_in), abs(self.x_i_in)) + max(self.r_in, self.r_i_in), max(abs(self.y_in), abs(self.y_i_in)) + max(self.r_in, self.r_i_in))

if __name__ == "__main__":
    # '''
    # Add menu here as mentioned in the sample output section of the assignment document.
    # '''
    # pass

    ver = int(input("verbose? 1 to plot, 0 otherwise: ")) # asking verbose

    n = int(input("Enter the number of test cases: ")) # asking number of test cases

    for i in range(n) :

        if ver == 0 :

            ty = int(input("\nEnter type of shape (polygon = 0/circle = 1): ")) # asking type

            if ty == 0 :

                side = int(input("Enter the number of sides: ")) # if polygon then asking number of sides

                l1 = []

                # inputting side

                for i in range(side) :

                    a = input("enter (x" + str(i + 1) + ", y" + str(i + 1) + "): ")

                    l2 = a.split(" ")

                    l1.append([float(l2[0]), float(l2[1]), 1])

                # making array

                d = np.array(l1)

                h = Polygon(d)

                que = int(input("Enter the number of queries: ")) # asking queries

                for i in range(que) :

                    print("\nEnter Query:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S sx (sy)\n4) P\n")

                    z = input()

                    lst1 = z.split(" ")

                    for i in range(1, len(lst1)) :

                        lst1[i] = float(lst1[i])

                    # query based calling of functions

                    if lst1[0] == "T" :

                        if len(lst1) == 2 :

                            # printing previous list

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) : 
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.translate(lst1[1], lst1[1])

                            # printing final list

                            for i in range(side) :

                                print(x_fin[i])
                                
                            for i in range(side) : 
                                
                                print(y_fin[i], end = " ")

                        elif len(lst1) == 3 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) : 
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.translate(lst1[1], lst1[2])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                    elif lst1[0] == "R" :

                        if len(lst1) == 2 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.rotate(lst1[1])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 3 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.rotate(lst1[1], lst1[2])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 4 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.rotate(lst1[1], lst1[2], lst1[3])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                    elif lst1[0] == "S" :

                        if len(lst1) == 2 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.scale(lst1[1], lst1[1])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 3 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.scale(lst1[1], lst1[2])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                    elif lst1[0] == "P" :

                        h.plot()

            elif ty == 1 :

                a = input("Enter the x and y cordinate of the center along with the radius : ") # if shape is circle then asking for center and radius

                l1 = a.split(" ")

                l2 = []

                for item in l1 :

                    l2.append(float(item))

                h = Circle(l2[0], l2[1], l2[2])

                que = int(input("Enter the number of queries: ")) # asking query

                # query based function calling

                for i in range(que) :

                    print("\nEnter Query:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S sx (sy)\n4) P\n")

                    z = input()

                    lst1 = z.split(" ")

                    for i in range(1, len(lst1)) :

                        lst1[i] = float(lst1[i])

                    if lst1[0] == "T" :

                        if len(lst1) == 2 :

                            # printing previous values

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.translate(lst1[1], lst1[1])

                            # printing final values

                            print(fin_x, fin_y, fin_r)

                        elif len(lst1) == 3 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.translate(lst1[1], lst1[2])

                            print(fin_x, fin_y, fin_r)

                    elif lst1[0] == "R" :

                        if len(lst1) == 2 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.rotate(lst1[1])

                            print(fin_x, fin_y, fin_r)

                        elif len(lst1) == 3 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.rotate(lst1[1], lst1[2])

                            print(fin_x, fin_y, fin_r)

                        elif len(lst1) == 4 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.rotate(lst1[1], lst1[2], lst1[3])

                            print(fin_x, fin_y, fin_r)

                    elif lst1[0] == "S" :

                        print(float(h.x_in), float(h.y_in), float(h.r_in))

                        fin_x, fin_y, fin_r = h.scale(lst1[1])

                        print(fin_x, fin_y, fin_r)

                    elif lst1[0] == "P" :

                        h.plot()

        elif ver == 1 :

            ty = int(input("\nEnter type of shape (polygon = 0/circle = 1): "))

            if ty == 0 :

                side = int(input("Enter the number of sides: "))

                l1 = []

                for i in range(side) :

                    a = input("enter (x" + str(i + 1) + ", y" + str(i + 1) + "): ")

                    l2 = a.split(" ")

                    l1.append([float(l2[0]), float(l2[1]), 1])

                d = np.array(l1)

                h = Polygon(d)

                que = int(input("Enter the number of queries: "))

                for i in range(que) :

                    print("\nEnter Query:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S sx (sy)\n4) P\n")

                    z = input()

                    lst1 = z.split(" ")

                    for i in range(1, len(lst1)) :

                        lst1[i] = float(lst1[i])

                    if lst1[0] == "T" :

                        if len(lst1) == 2 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.translate(lst1[1], lst1[1])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 3 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("") # plot is at theend here now because ver is 1

                            x_fin, y_fin = h.translate(lst1[1], lst1[2])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        h.plot()

                    elif lst1[0] == "R" :

                        if len(lst1) == 2 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.rotate(lst1[1])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 3 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.rotate(lst1[1], lst1[2])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 4 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.rotate(lst1[1], lst1[2], lst1[3])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        h.plot()

                    elif lst1[0] == "S" :

                        if len(lst1) == 2 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.scale(lst1[1], lst1[1])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        elif len(lst1) == 3 :

                            for i in range(side) :

                                print(float((h.x_in)[i]), end = " ") 
                                
                            for i in range(side) :
                                
                                print(float((h.y_in)[i]), end = " ")

                            print("")

                            x_fin, y_fin = h.scale(lst1[1], lst1[2])

                            for i in range(side) :

                                print(x_fin[i], end = " ")

                            for i in range(side) :

                                print(y_fin[i], end = " ")

                        h.plot()

                    elif lst1[0] == "P" :

                        h.plot()

            elif ty == 1 :

                a = input("Enter the x and y cordinate of the center along with the radius : ")

                l1 = a.split(" ")

                l2 = []

                for item in l1 :

                    l2.append(float(item))

                h = Circle(l2[0], l2[1], l2[2])

                que = int(input("Enter the number of queries: "))

                for i in range(que) :

                    print("\nEnter Query:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S sx (sy)\n4) P\n")

                    z = input()

                    lst1 = z.split(" ")

                    for i in range(1, len(lst1)) :

                        lst1[i] = float(lst1[i])

                    if lst1[0] == "T" :

                        if len(lst1) == 2 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.translate(lst1[1], lst1[1])

                            print(fin_x, fin_y, fin_r)

                        elif len(lst1) == 3 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.translate(lst1[1], lst1[2])

                            print(fin_x, fin_y, fin_r)

                        h.plot()

                    elif lst1[0] == "R" :

                        if len(lst1) == 2 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.rotate(lst1[1])

                            print(fin_x, fin_y, fin_r)

                        elif len(lst1) == 3 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.rotate(lst1[1], lst1[2])

                            print(fin_x, fin_y, fin_r)

                        elif len(lst1) == 4 :

                            print(float(h.x_in), float(h.y_in), float(h.r_in))

                            fin_x, fin_y, fin_r = h.rotate(lst1[1], lst1[2], lst1[3])

                            print(fin_x, fin_y, fin_r)

                        h.plot()

                    elif lst1[0] == "S" :

                        print(float(h.x_in), float(h.y_in), float(h.r_in))

                        fin_x, fin_y, fin_r = h.scale(lst1[1])

                        print(fin_x, fin_y, fin_r)

                        h.plot()

                    elif lst1[0] == "P" :

                        h.plot()

    print("\n\nThank You!")
from math import sqrt

class Scaling:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.curr_area = self.width * self.height
        self.target_area = 0
        self.ratio = 0

    def set_height(self):
        self.height = input("Enter height -->  ")
        self.height = float(self.height)

    def set_width(self):
        self.width = input("Enter width -->  ")
        self.width = float(self.width)

    def set_target_area(self):
        self.target_area = input("Enter target area size -->  ")
        self.target_area = float(self.target_area)

    def calc_ratio(self):
        print("\nCalculating ratio...")
        self.ratio = sqrt(self.target_area/(self.width*self.height))
        print("Your ratio is: {0:.3f}\n".format(self.ratio))

    def print_final(self):
        print("#"*24)
        print("\nNEW WIDTH: {0:.7f}mm\n".format(self.width*self.ratio))
        print("#"*24)
        print("\nNEW HEIGHT: {0:.7f}mm\n".format(self.height*self.ratio))
        print("#"*24)
        print("\nLet's just make sure this is correct...\n")
        print("Target area -->  {}".format(self.target_area))
        self.final_area = (self.height*self.ratio)*(self.width*self.ratio)
        print("Final area  -->  {}\n".format(self.final_area))

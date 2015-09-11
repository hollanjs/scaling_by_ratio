from scaling_by_ratio import Scaling

calc = Scaling() # instatiate the object
calc.set_target_area() # set the area as a constant for the loop

not_done = True

# run calculations till your eyes bleed
while(not_done):
    calc.set_width()
    calc.set_height()
    calc.calc_ratio()
    calc.print_final()
    finished = input("type 'done' if you are finished. \
                          \nOtherwise, press enter: ")
    if finished == 'done':
        not_done = False
    

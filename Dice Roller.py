import random

def dice_roller():
    
    rolls = 0
    total = 0
    
    dice_input = input("Please input your dice roll, for example '3d6': ").split("d")
            
    dice_num = int(dice_input[0])
    dice_max = int(dice_input[1])
    
    while rolls < dice_num:
        
        dice = (random.randint(1, dice_max))
        total += dice 
        rolls += 1
        print("Dice {} is: {}".format(rolls,dice))
    
    print("Total is: {}".format(total))
   

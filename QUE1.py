#Write  a python program which will keep adding a stream of numbers inputted by teh user.The adding stops as soon as user presses the q in a keyboatrd?????

sum = 0 
while(True):
    userInput = input("Enter the price of the item or OR press q to quit")

    if(userInput != 'q'):
        sum = sum + int(userInput)
        print(f"The Total sum so far of the item is : {sum}")
    else:
        print(f"Your Bill total is {sum}. Thanks for shopping with us")   
        break

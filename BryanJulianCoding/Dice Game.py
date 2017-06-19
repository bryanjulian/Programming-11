import random
print ("Welcome to Bryan's Dice Rolling Extravaganza!")
my_input = input("Do you want to roll, Yes or No?:")
times_rolled = 0
done = False
while not done: 
    if my_input.lower() == "yes":
        print (random.randint(1,6))
        times_rolled += 1
        print ("You have rolled", times_rolled,"times.")
    continue_rolling = input("Keep rolling, Yes or No?")
    if continue_rolling.lower() == "no":
        done = True
        print ("Quit.")
        

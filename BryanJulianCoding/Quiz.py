print ("Quiz Time!")
print ("Question 1:")
answer1 = int(input("What is 20*6+13?"))
# Must put a space inbetween the question and your answer.
if answer1 == 133:
    print ("Correct!")
    answer1 = 1
else:
    print ("Wrong.")
    answer1 = 0
print ("Question 2:")
answer2 = int(input("What is 12/4-37?"))
if answer2 == -34:
    print ("Correct!")
    answer2 = 1
else:
    print ("Wrong.")
    answer2 = 0
print ("Question 3:")
answer3 = input("Who is Batman's most iconic sidekick?")
if answer3.lower() == "robin":
    print ("Correct!")
    answer3 = 1
else:
    print ("Wrong.")
    answer3 = 0
print ("Question 4:")
print ("How many heroes are there in Overwatch? As of Nov. 2nd 2016. \nA: 13 \nB: 22 \nC: 27 \nD: 32")
answer4 = input("Answer:")
if answer4.lower() == "b":
    print ("Correct!")
    answer4 = 1
else:
    print ("Wrong.")
    answer4 = 0
print ("Question 5:")
answer5 = input("If I have 17 potatoes and i give 5 away, how many do I have left?")
if answer5.lower() == "12":
    print ("Correct!")
    answer5 = 1
else:
    print ("Wrong.")
    answer5 = 0
print ("Finish!")
print ("You got,")
print (answer1 + answer2 + answer3 + answer4 + answer5,"answers correct.")
print ((answer1 + answer2 + answer3 + answer4 + answer5)/5*100,"%")


from random import *
User_Input = input("How tired are you? (Not/Little/Somewhat/Quite/Very): ")
ListofPossibleInputs = ["Not", "Little", "Somewhat", "Quite", "Very"]
tiredfactor = 0
for x in range (len(ListofPossibleInputs)):
    if User_Input == ListofPossibleInputs[x]:
        tiredfactor = x
random_multiplier = randint(1, 10)
if (random_multiplier * tiredfactor) > 10:
    print("Go to bed, sleepyhead :3")
else:
    print("You'll be fine, surely... ")
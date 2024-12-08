User_input1 = int(input("Give me a number: "))
User_input2 = int(input("Give me a second number: "))
User_Operation = input("What do you want to do with them? Your options are: Add (A), Subtract (S), Multiply (M), Divide (D), Exponentiate (E), or Root (R): ")
if User_Operation == "A":
    Output = User_input1 + User_input2
elif User_Operation == "S":
    Output = User_input1 - User_input2
elif User_Operation == "M":
    Output = User_input1 * User_input2
elif User_Operation == "D":
    Output = User_input1 / User_input2
elif User_Operation == "E":
    Output =  User_input1 ** User_input2
elif User_Operation == "R":
    Output = User_input1 ** (1/User_input2)
print("Your result is:", Output)
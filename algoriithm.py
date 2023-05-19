# Set num1 as 713
num1 = 713

# Set num2 as 9999
num2 = "9990"

# Check if num2 consists of '9's
if all(char == '9' for char in num2):
    # Calculate Res1
    Res1 = num1 - 1

    # Calculate Res2
    Res2 = int(num2) - Res1

    # Concatenate Res1 and Res2 into Answer
    Answer = str(Res1) + str(Res2)

    # Print
    print(Answer)
else:
    print("Invalid input: num2 must consist of a string of '9's")
    print("\n Done")

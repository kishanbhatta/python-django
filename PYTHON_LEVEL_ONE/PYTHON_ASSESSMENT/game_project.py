import random
# GET GUESS
def get_guess():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input("What is your guess?"))


# GENERATE COMPUTER CODE 123
def generate_code():
    '''
    generates a 3 digit list for the code.
    '''
    digits = [str(num) for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits)
    #Then grab the first three
    return digits[:3]

# GENERATE THE CLUES
def gen_clues(code, user_guess):
    '''
    Takes in a user guess and code then compares the numbers in a loop and creates
    a list if clues according to the matching parameters.
    '''

    if user_guess == code:
        return "CODE CRACKED!"

    clues = []
    # Compare guess to code
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return["Nope"]
    else:
        return clues

# RUN GAME logical
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
# Create a Secret Code to start the Game
secret_code = generate_code()
print("Code has been generated, please guess a 3 digit number")

# Empty Clue Report to Start with
clue_report = []

# Keep asking until the user has gotten it right!
while clue_report != "CODE CRACKED!":

    #Ask for guess
    guess = get_guess()

    # Give the clues 
    clue_report = gen_clues(guess,secret_code)
    print("here is the result of your guess:")
    for clue in clue_report:
        print(clue)

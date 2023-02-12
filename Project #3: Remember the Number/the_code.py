import random
import time
import os

def generate_number():

    the_generated_number = ""
    number_length = int(input("How many numbers in a sequence do you want to remember? Enter a number: "))

    statement = "You must remember this number in 15 seconds that contains " + str(number_length) + " digits:"
    print(statement)
    
    # time.sleep(10)
    # os.system('cls')


    for i in range(0, number_length):

        if i == 0:
            number_digit = random.randint(1, 9)
            str_number_digit = str(number_digit)
            the_generated_number = the_generated_number + str_number_digit
        else:
            number_digit = random.randint(0, 9)
            str_number_digit = str(number_digit)
            the_generated_number = the_generated_number + str_number_digit

    return the_generated_number
    
print(generate_number())

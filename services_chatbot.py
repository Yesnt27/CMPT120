# Services Chatbot
# Kenny Nguyen
# September 11th 2024
import random

for n in range (0,3):

    user_name = input("What is your name: ")

    print("Nice to meet you, ",user_name)
    print("Welcome to the fitness recreational centre for Mars!")

    print("Some options for inquiries are 'programs','times','sports'\n")
    questions = input("What do you need help with?\n")
    questions = questions.lower()

    #are you sure you want to register for this program
    yes_ans = ["yes",'y']
    

    no_ans = ["no",'n']
  

    

    if "programs" in questions:
        inquiry1 =input('Programs list: Yoga, Aquafit, ')
        if inquiry1 in yes_ans: 


            confirmation = input("Are you sure you want to register for this program? Please enter [Yes/No] > ")
            confirmation = confirmation.lower()
            confirmation = confirmation.strip()
            while (confirmation is not yes_ans or no_ans):
                confirmation = input("Invalid input. Please enter a valid yes or no value > ")

    elif "times" in questions:
        print("times: ")
    elif "sports" in questions:
        print("sports")
    else:
        randoms = ["Please refer to John at 779-854-669","Please refer to Samantha at 778-866-559","Please refer to Lacy at 604-435-753"]
        randoms = random.choice(randoms)
        print(randoms)









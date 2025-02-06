# List of Questions
# Score the answers

# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score


import random

questions= {
    "What is the keyword to define a function in python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for python files?": ".py",
    "which symbol is used to comment in python?": "#",
    "what function is used to get input from the user?": "input",
    "How do you start a for loop in python?": "for",
    "What is the output of 2**3 in python?": "8",
    "What keyword is used to import a module in python?":"import",
    "What does the len() function return?":"length",
    "What is the result of 10//3 in python?": "3",
    "What keyword is used to create a class in Python?": "class",
    "What is the name of the first index in Python lists?": "zero",
    "Which built-in function is used to sort a list?": "sorted",
    "What is the name of the default Python interpreter?": "cpython",
    "Which keyword is used to handle exceptions in Python?": "try",
    "What is the file extension for compiled Python files?": ".pyc",
    "Which function returns the number of items in a list?": "len",
    "What is the term for removing whitespace from the start and end of a string?": "strip",
    "What keyword is used to define an anonymous function?": "lambda",
    "What method is used to add an item to a list?": "append",
    "What is the default value of the variable i in a for loop?": "zero",
    "Which method is used to find the highest value in a list?": "max",
    "What keyword is used to delete an object in Python?": "del",
    "Which keyword is used to define a generator function?": "yield",
    "What function is used to open a file in Python?": "open",
    "What symbol is used to denote a tuple in Python?": "()",
    "What keyword is used to check for membership in a list?": "in",
    "Which function converts a string to lowercase?": "lower",
    "What keyword creates a new instance of a class?": "self",
    "Which operator is used for string concatenation?": "+"
}

def trivia_game():
    questions_list=list(questions.keys())
    total_questions=5
    score=0

    selected_questions=random.sample(questions_list,total_questions)

    for idx,question in enumerate(selected_questions):
        print(f"{idx+1}.{question}")
        user_answer=input("your answer: ").lower().strip()

        correct_answer=questions[question]

        if user_answer ==correct_answer.lower():
            print("Correct!\n")
            score+=1
        else:
            print(f"Worng the correct answer is : {correct_answer}.\n")
    print(f"Game over! your final score is {score}/{total_questions}")

trivia_game()




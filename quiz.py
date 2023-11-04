# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
        "answer": "Blue Whale"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")
        
        user_answer = input("Your answer (1/2/3/4): ")
        
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                user_answer = question["options"][user_answer - 1]
                if user_answer == question["answer"]:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {question['answer']}\n")
            else:
                print("Invalid input. Please choose a valid option.\n")
        else:
            print("Invalid input. Please enter a number.\n")
    
    print(f"You got {score} out of {len(questions)} questions correct!")

# Start the quiz
if __name__ == "__main__":
    run_quiz()
1

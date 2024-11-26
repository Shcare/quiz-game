questions = [
{
    'prompt': 'What is the capital of France?',
    'options': ['A. Paris', 'B. London', 'C. Berlin', 'D. Madrid'],
    'answer': 'A'
},
{
    'prompt': 'Which language is primarily spoken in Brazil?',
    'options': ['A. Spanish', 'B. Portuguese', 'C. English', 'D. French'],
    'answer': 'B'
},
{
    'prompt': 'What is the smallest prime number?',
    'options': ['A. 1', 'B. 2', 'C. 3', 'D. 5'],
    'answer': 'B'
},
{
    'prompt': 'Who wrote "to kill a Mockingbird"?',
    'options': ['A. Harper Lee', 'B. Mark Twain', 'C. J.K. Rowling', 'D. Ernest Homingway'],
    'answer': 'A'
},
{
    'prompt': ' Which planet is closest to the Sun?',
    'options': ['A. Harper Lee', 'B. Mark Twain', 'C. J.K. Rowling', 'D. Ernest Homingway'],
    'answer': 'A'
},
{
    "prompt": "What is the largest organ in the human body?",
    "options": ["A. Heart", "B. Liver", "C. Lungs", "D. Skin"],
    "answer": "D"
},
{
    "prompt": "What is the chemical symbol for water?",
    "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
    "answer": "A"
},
{
    "prompt": "Which country hosted the 2022 FIFA World Cup?",
    "options": ["A. Qatar", "B. Russia", "C. Brazil", "D. Germany"],
    "answer": "A"
}

]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer = input('Enter your answer (A, B, C or D):').upper()
        if answer == question['answer']:
            print('Correct, Wow!!')
            score += 1
        else:
            print('Wrong, the correct answer was', question['answer'],'\n')   

    print (f'you got {score} out of {len(questions)} questions correct.')

run_quiz(questions)
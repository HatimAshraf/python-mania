#prepare questions to ask   
#save the answer to the questions
#make sure questions will be pop randomly
#ask the questions
#check if the answer is correct
#keep track of the score
#display the score

import random

questions = {
  "What is the capital of France?": "Paris",
  "How many planets in the solar system?": "8",
  "What is the largest mammal?": "Blue Whale",
  "What is the largest ocean?": "Pacific Ocean",
  "Which country won 2002 FIFA World Cup?": "Brazil",
  "who has won the most ATP titles in Mens Singles?":"Djocovic",
  "what is 2*2?":"4"
} 

def play_game():
  print("Welcome to the Trivia Game!")
  questions_list = list(questions.keys())
  score = 0
  total_questions = 5
  random_questions = random.sample(questions_list, total_questions)

  for question in random_questions:
    print(question)
    answer = input("Enter your answer: ")
    if questions[question].lower() == answer.lower():
      score += 1
      print("Correct!")
    else:
      print("Incorrect!")
  print(f"Your final score is {score}/{total_questions}")

play_game()
  
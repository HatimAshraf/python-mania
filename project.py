#prepare questions to ask   
#save the answer to the questions
#make sure questions will be pop randomly
#ask the questions
#check if the answer is correct
#keep track of the score
#display the score
#ask if the user wants to play again
#ask how many questions the user wants to answer
#continue till the answer is no

import random

questions = {
  "What is the capital of France?": "Paris",
  "How many planets in the solar system?": "8",
  "What is the largest mammal?": "Whale",
  "What is the largest ocean?": "Pacific",
  "Which country won 2002 FIFA World Cup?": "Brazil",
  "who has won the most ATP titles in Mens Singles?":"Djocovic",
  "what is 2*2?":"4"
} 

def play_game(num_questions):
  print("Welcome to the Trivia Game!")
  questions_list = list(questions.keys())
  score = 0
  random_questions = random.sample(questions_list, num_questions)

  for question in random_questions:
    print(question)
    answer = input("Enter your answer: ")
    correct_answer = questions[question]
    if answer.lower().strip() == correct_answer.lower():
      score += 1
      print("Correct!")
    else:
      print(f"Incorrect!, The correct answer is {correct_answer}")
  print(f"Your final score is {score}/{num_questions}")

if __name__ == "__main__":  
  print("How many questions would you like to answer?")
  total_questions = int(input("Enter the number of questions (1-6): "))
  play_game(total_questions)
  play_again = input("Would you like to play again? (yes/no): ")
  while play_again.lower() == "yes" or play_again.lower() == "y":
    print("How many questions would you like to answer?")
    total_questions = int(input("Enter the number of questions (1-6): "))
    play_game(total_questions)
    play_again = input("Would you like to play again? (yes/no): ")
  print("Thanks for playing!")  
    
  



  
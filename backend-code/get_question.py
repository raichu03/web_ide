import json
import random

def questions(difficulty: str):
    with open(f'questions/{difficulty}.json', 'r') as file:
        data = json.load(file)
        
    random_question = random.choice(data[difficulty])
    return random_question

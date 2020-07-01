#!/usr/bin/ python3
'''Author: Michael
'''

import requests

def main():
    '''this is a jeopardy game'''
    player = input('Please enter your name\n')
    rounds = int(input("Please enter a number of rounds\n"))
    counter = 0
    score = 0
    base_URI = 'http://jservice.io/'
    rand = requests.get(f'{base_URI}/api/random?count={rounds}')
    random_Q = rand.json()

    for i in range(rounds):
        value = random_Q[i]['value']
        print(random_Q[i]['answer'])
        player_answer = input(random_Q[i]["question"] + "\n")
        if player_answer.lower() == random_Q[i]["answer"].lower():
            print("correct!")
            counter += 1
            score += value
        else:
            print(f"No, that's not it. The correct answer was {random_Q[i]['answer']}")
            score -= value

    print(f'{player}, you got {counter} questions correct.  Your score is {score}')


if __name__ == "__main__":
    main()

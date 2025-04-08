from art import logo
from art import vs
from game_data import data
import random
print(logo)
user_guessed_correct=False
currentscore=0
while not user_guessed_correct:
    A=random.choice(data)
    B=random.choice(data)
    print(f"Compare A: {A["name"]},a {A["description"]}, from {A["country"]}")
    print(vs)
    print(f"Against B: {B["name"]},a {B["description"]}, from {B["country"]}")
    choice=input("Who has more followers? Type 'A' or 'B':")
    print(choice)
    if choice=="A" and A["follower_count"]>B["follower_count"] or choice=="B" and B["follower_count"]> A["follower_count"]:
        currentscore+=1
        print(f"You're right! Current score= {currentscore}.")
    else:
        user_guessed_correct=True
        print(f"Sorry, that's wrong. Final Score={currentscore}" )
        break

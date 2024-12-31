import random
choices = ["Rock", "Paper", "Scissors"] 

#score tracking , make two variables;

player_score=0
ai_score=0

print("Welcome to Rock, Paper , Scissors with AI")

while True:
    players_choice= input(" Enter your choice(Rock, Paper, Scissors or Quit to exit): ").capitalize()

    if players_choice=="Quit":
        print("Thanks for playing !")
        print(f"Final-Scores - You:{player_score}, AI:{ai_score}")
        break
    if players_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice! Please choose Rock ,Paper or Scissors.")
        continue

    ai_choice=random.choice(choices)
    print(f"AI choose:{ai_choice}")

    if players_choice==ai_choice:
        print("It's a tie ")
    elif (players_choice == "Rock" and ai_choice == "Scissors") or \
        (players_choice == "Scissors" and ai_choice == "Paper") or \
        (players_choice == "Paper" and ai_choice == "Rock"):
         print("You Win!")
         player_score+=1 

    else:
        print("AI wins")
        ai_score+=1

    print(f"Final Scores - You:{player_score}, AI:{ai_score}")
    print("-"*30)


    

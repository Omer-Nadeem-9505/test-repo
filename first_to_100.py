import random


def roll_dice():
    return random.randint(1, 6)

def play_game():
    player1_score = 0
    player2_score = 0
    target_score = 100    
            
    while player1_score < target_score and player2_score < target_score:
        input("Player 1, press Enter to roll the dice...")
        roll = roll_dice()
        if player1_score + roll <= 100:
            player1_score += roll
            print(f"Player 1 rolled a {roll}, Total Score: {player1_score}\n")
        else :
            print(f"Player 1 rolled a {roll}, Total Score can't exeed 100 current score: {player1_score}\n")
        if player1_score >= target_score:
            print("🎉 Player 1 wins! 🎉")
            break
        
        input("Player 2, press Enter to roll the dice...")
        roll = roll_dice()
        if player2_score + roll <= 100:
            player2_score += roll
            print(f"Player 2 rolled a {roll}, Total Score: {player2_score}\n")
        else :
            print(f"Player 2 rolled a {roll}, Total Score can't exeed 100 current score: {player2_score}\n")
        if player2_score >= target_score:
            print("🎉 Player 2 wins! 🎉")
            break
            

play_game() 
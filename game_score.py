player_name = input("Enter the name of the player:")
games_played = int(input("Enter the no.of games played:"))
total_score = int(input("Enter the total score:"))
average_score = total_score/ games_played

print("\n Player Details")
print(f"Player: {player_name}")
print(f"Games played: {games_played}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
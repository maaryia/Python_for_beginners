def main():
    # Step 1: Input Reading
    n = int(input("Enter the number of players: "))  # Number of players
    games = list(map(int, input("Enter the number of games for each player: ").split()))  # Number of games

    # Step 2: Identify Eligible Players
    eligible_players = [game for game in games if game <= 2]

    # Step 3: Calculate the Number of Teams
    number_of_teams = len(eligible_players) // 3

    # Step 4: Output the Result
    print(number_of_teams)

if __name__ == "__main__":
    main()


# def max_teams(players):
#     max_team = 0
#     for player in players:
#         if player <= 2:
#             max_team += 1
#     return max_team 

# n = int(input("Enter the number of players: ")) 
# players = []

# while True:
#     try:
#         players_input = input("Enter the number: ").split()
#         players = [int(player) for player in players_input]
#         break
#     except ValueError:
#         print("Invalid input. Please enter numbers separated by spaces.")

# max_teams = max_teams(players)
# print("The maximum number of teams is:", max_teams)
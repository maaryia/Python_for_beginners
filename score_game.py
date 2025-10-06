def rasht_score():
    num_games = 5
    points = 0
    wins = 0

    for i in range(num_games):
        while True:
            try:
                score = int(input(f"Please enter your score for game {i + 1} (0, 1, 3): "))
                if score not in [0, 1, 3]:
                    raise ValueError("Invalid input! Only 0, 1, or 3 are allowed.")
                break
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                print("\nInput interrupted. Please enter numbers only.")
            except Exception as e:
                print("Unexpected error:", e)

        points += score
        if score == 3:
            wins += 1

    print(f"Total score: {points}")
    print(f"Total wins: {wins}")

rasht_score()

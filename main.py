import pandas as pd

df = pd.read_csv("atp_tennis.csv")

winner_by_event = []

for index, row in df.iterrows():
    winner = row["Winner"]
    player1 = row["Player_1"]
    player2 = row["Player_2"]

    if player1 == winner:
        winner_by_event.append(1)
    else:
        winner_by_event.append(0)

print(winner_by_event)
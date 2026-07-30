import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("atp_tennis.csv")

winner_by_event = []

#filter valid games
condition = (df["Rank_1"] != -1) & (df["Rank_2"] != -1) & (df["Pts_1"] != -1) & (df["Pts_2"] != -1)
filtered_df = df[condition]

#manage y
for index, row in filtered_df.iterrows():
    winner = row["Winner"]
    player1 = row["Player_1"]
    player2 = row["Player_2"]

    if player1 == winner:
        winner_by_event.append(1)
    else:
        winner_by_event.append(0)

#manage x
x = pd.concat([filtered_df[["Rank_1", "Rank_2","Pts_1","Pts_2"]], pd.get_dummies(filtered_df[["Surface"]])], axis=1)
y = winner_by_event

model = RandomForestClassifier()
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=42)
model.fit(X_train, Y_train)
prediction = model.predict(X_test)

print(sum(y)/len(y))
print(prediction)
print(accuracy_score(Y_test, prediction))
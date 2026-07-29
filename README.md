# atp_tennis_match_predictor_ml

ATP Tennis (2000–2026) — Machine Learning Project

Dataset: ATP Tennis daily-update dataset, ~68,000 rows, one row per match (Tournament, Date, Series, Court, Surface, Round, Best of, Player_1, Player_2, Winner, Rank_1, Rank_2, Pts_1, Pts_2, Odd_1, Odd_2, Score).

Goal: predict which player wins a given match, based only on information known **before** the match is played — not the score or outcome of the match itself.

In this project, you:

- Take the dataset
- Clean and preprocess the data using:
  - Pandas
  - NumPy

Then:

- Learn and use the Scikit-learn (sklearn) library
- Train and test a classification model using:
  - `.fit()` method for training
  - `.predict()` method for predictions

## Features (X) and target (y)

- **X (features):** `Rank_1`, `Rank_2`, `Pts_1`, `Pts_2`, `Surface`, `Court`, `Series`, `Round`, `Best of`
- **y (target):** did `Player_1` win the match? (1/0, derived from `Winner`)

**Excluded from X (data leakage):** `Score`, `Winner` — these are only known **after** the match has been played. `Odd_1`/`Odd_2` are also excluded, since they're a bookmaker's own prediction, not raw match information.

**Known caveat to check before training:** whether `Player_1`/`Player_2` order is arbitrary or systematically tied to rank — if the higher-ranked player is consistently listed as `Player_1`, the model could learn that ordering instead of real skill signals, so this should be verified (and corrected if needed) during preprocessing.

## Bonus points

- Create visualizations using Matplotlib
- Add performance metrics to evaluate the model (accuracy, precision, recall, etc.)
- Analyze results and interpret what the model is learning

## Goal

Understand the full machine learning pipeline:

- data collection → cleaning → training → evaluation → visualization

# ai_health_impact_ml

AI Impact on Health — Machine Learning Project

Dataset: `AI_Impact_on_Health_Dataset_5000_Enhanced.csv` (5000 participants, tracking demographics, AI health tool usage, and health outcomes before/after).

Goal: predict whether a participant's health outcome falls into **Declined / No Change / Improved / Highly Improved** (`Improvement_Category`), based on who they are and how they use AI health tools — _not_ based on the health scores that were used to compute that label.

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

- **X (features):** `Age`, `Gender`, `Chronic_Condition`, `BMI`, `AI_Tool_Type`, `AI_Health_App_Usage_Hours_Per_Week`, `Exercise_Hours_Per_Week`
- **y (target):** `Improvement_Category`

**Excluded from X (data leakage):** `Health_Score_Before_AI`, `Health_Score_After_AI`, `Improvement`, `Improvement_Percentage`, `Improvement_Per_AI_Hour`, `Satisfaction_Score`, `Satisfaction_Level`, `Risk_Category` — these are all derived from or tied to the same outcome you're trying to predict.

## Bonus points

- Create visualizations using Matplotlib
- Add performance metrics to evaluate the model (accuracy, precision, recall, etc.)
- Analyze results and interpret what the model is learning

## Goal

Understand the full machine learning pipeline:

- data collection → cleaning → training → evaluation → visualization

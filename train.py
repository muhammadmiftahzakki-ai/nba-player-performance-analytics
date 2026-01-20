import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load player dataset
df = pd.read_csv("players_master.csv")

# Features & target (SESUI DATASET ASLI)
X = df[["BASE_MIN", "BASE_AGE", "BASE_GP"]]
y = df["BASE_PTS"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Sample prediction (REALISTIS)
sample_prediction = model.predict([[32, 27, 70]])
print("Sample prediction (points):", sample_prediction[0])

# Save model
joblib.dump(model, "nba_player_points_model.pkl")

print("Model regresi berhasil disimpan!")

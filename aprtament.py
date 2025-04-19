import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
df = pd.read_csv("apartments.csv")

# 2. Show the first 5 rows
print("📊 Preview of data:")
print(df.head())

# 3. Show basic info and stats
print("\n📈 Data info:")
print(df.info())

print("\n📊 Statistics:")
print(df.describe())

# 4. Plot price vs. size
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="size_m2", y="price", hue="area")
plt.title("Apartment Price vs. Size (m²)")
plt.xlabel("Size (m²)")
plt.ylabel("Price (DKK)")
plt.tight_layout()
plt.show()

# 5. Prepare data for prediction
# Features (X) = m² and rooms | Target (y) = price
X = df[["size_m2", "rooms"]]
y = df["price"]

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Save model to file
joblib.dump(model, "apartment_model.pkl")
print("💾 Model saved to apartment_model.pkl")


# Predict on test set
y_pred = model.predict(X_test)

# Evaluation metrics
print("\n📉 Model Evaluation:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# 6. Predict a new apartment
new_apartment = [[80, 3]]  # 80 m², 3 rooms
predicted_price = model.predict(new_apartment)

print(f"\n💰 Predicted price for 80 m² & 3 rooms: {int(predicted_price[0])} DKK")

print("\n✅ Script finished.")

# 7. Load the saved model and make prediction from user input
print("\n🔍 Try your own prediction:")

try:
    user_size = float(input("Enter apartment size in m²: "))
    user_rooms = int(input("Enter number of rooms: "))
    loaded_model = joblib.load("apartment_model.pkl")
    result = loaded_model.predict([[user_size, user_rooms]])
    print(f"💰 Estimated price: {int(result[0])} DKK")
except Exception as e:
    print("❌ Error during prediction:", e)

import joblib

print("🏠 Apartment Price Prediction")

try:
    # Ask user for input
    size = float(input("Enter apartment size in m²: "))
    rooms = int(input("Enter number of rooms: "))

    # Load the trained model
    model = joblib.load("apartment_model.pkl")

    # Predict price
    predicted_price = model.predict([[size, rooms]])
    print(f"\n💰 Estimated price: {int(predicted_price[0])} DKK")

except Exception as e:
    print("❌ Error during prediction:", e)

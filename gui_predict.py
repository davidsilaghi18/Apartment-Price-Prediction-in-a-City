import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model
model = joblib.load("apartment_model.pkl")

# Create window
window = tk.Tk()
window.title("🏠 Apartment Price Predictor")
window.geometry("300x250")

# Labels
tk.Label(window, text="Size in m²:").pack(pady=5)
entry_size = tk.Entry(window)
entry_size.pack()

tk.Label(window, text="Number of rooms:").pack(pady=5)
entry_rooms = tk.Entry(window)
entry_rooms.pack()

# Function to predict
def predict_price():
    try:
        size = float(entry_size.get())
        rooms = int(entry_rooms.get())
        prediction = model.predict([[size, rooms]])
        price = int(prediction[0])
        messagebox.showinfo("Estimated Price", f"💰 {price} DKK")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Predict button
tk.Button(window, text="Predict Price", command=predict_price).pack(pady=20)

# Run app
window.mainloop()

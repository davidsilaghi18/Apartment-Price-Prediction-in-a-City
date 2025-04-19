# 🏠 Apartment Price Prediction in a City

This is a simple machine learning project that predicts the price of an apartment based on its size and number of rooms. It includes:

- 📊 Data visualization
- 🧠 Model training using Linear Regression
- 💾 Model saving/loading with Joblib
- 🖥️ GUI (Graphical User Interface) using Tkinter
- 🛠️ Compiled .exe version (Windows)

---

## 📂 Project structure

 Apartment Price Prediction in a City/ ├── apartments.csv # Dataset with apartment data ├── apartment.py # Script to train & evaluate model ├── apartment_model.pkl # Saved ML model ├── predict_only.py # Quick terminal-based prediction ├── gui_predict.py # GUI app using Tkinter └── README.md # This file

 
---

## ⚙️ How to use

### 1. Train the model
Run `apartment.py` to train the model and generate the file `apartment_model.pkl`.

```bash
python apartment.py

2. Predict using GUI
Run the GUI app:

bash

python gui_predict.py
Enter apartment size and number of rooms → you'll get an estimated price 💰

📦 .EXE version
The GUI version can be converted into a .exe using:

bash


pyinstaller --onefile --windowed gui_predict.py
This generates gui_predict.exe in the dist/ folder (not included here).

🧠 Technologies used
Python 3

Pandas

Matplotlib

Seaborn

scikit-learn

Tkinter

Joblib

PyInstaller (for .exe)

🧔 Made by
👨‍💻 David Silaghi – Student at Roskilde University (RUC)
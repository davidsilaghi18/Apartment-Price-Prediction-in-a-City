# Apartment-Price-Prediction-in-a-City
A project for Apartment Price Prediction in a City with python
# 🏠 Apartment Price Prediction in a City

This project uses machine learning to predict apartment prices based on their size and number of rooms. It includes data visualization, model training using Linear Regression, a graphical user interface (GUI) built with Tkinter, and an optional Windows executable (.exe) version using PyInstaller.

## 📊 Features

- Predict apartment price based on size and number of rooms
- Visualize data using Matplotlib and Seaborn
- Train a machine learning model with scikit-learn
- Save and load the trained model using Joblib
- GUI application with input fields and a predict button
- Create a .exe file to run the app without Python

## 🗂 Project Structure

Apartment Price Prediction in a City/ ├── apartments.csv # Dataset with apartment data ├── apartment.py # Main script: training, visualization, model saving ├── apartment_model.pkl # Trained model file (saved with Joblib) ├── predict_only.py # Simple prediction script for console use ├── gui_predict.py # GUI application using Tkinter └── README.md # Project documentation


## 🚀 How to Use

### Step 1 – Train the Model

Run the following command to train the model and create the model file:

python apartment.py

This will generate a file called `apartment_model.pkl`.

### Step 2 – Predict Using GUI

Run the following script:

python gui_predict.py

A window will appear where you can enter the apartment size and number of rooms.  
Click the "Predict Price" button to see the estimated price.

### Step 3 – Predict in the Terminal

If you want a simple terminal-based prediction tool, use:

python predict_only.py

## 🛠 Creating a .EXE File (Optional)

To generate a standalone executable file for Windows:

1. Install PyInstaller (if you haven't already):
pip install pyinstaller

2. Create the .exe file:
pyinstaller --onefile --windowed gui_predict.py

The .exe will be created inside the `dist/` folder as `gui_predict.exe`.  
Make sure to also copy the file `apartment_model.pkl` next to the `.exe`.

## 🧠 Technologies Used

- Python 3
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- Tkinter
- Joblib
- PyInstaller

## 👨‍💻 Author

**David Silaghi**  
Student at Roskilde University (RUC)

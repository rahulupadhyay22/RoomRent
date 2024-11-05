# 🏠 Room Rent Calculator

This Room Rent Calculator is a Python-based application that calculates the individual expense share for roommates based on total rent, food, and electricity charges. It features a GUI built with `tkinter` and an option to export results as a PDF file using `fpdf`.

## 📋 Features
- **Calculates total expenses** per person based on rent, food, and electricity costs.
- **Exports calculation results to a PDF file**.
- Simple and user-friendly **GUI for easy data entry**.

## 🛠️ Requirements
- **Python 3.x**
- **Packages**: `tkinter` (standard with Python), `fpdf`

## 🚀 Installation
1. **Install Python**: Download Python 3.x from [python.org](https://www.python.org/downloads/).
2. **Install `fpdf`**:
   ```bash
   pip install fpdf
   ```

## 📂 Setup
1. **Clone or download** this repository to your local machine.
2. **Navigate to the directory** and run:
   ```bash
   python room_rent_calculator.py
   ```

## 🖥️ Usage Guide

1. **Enter Values in the GUI**:
   - **Total Number of Persons** sharing the room.
   - **Total Rent** for the room.
   - **Total Food Expenses**.
   - **Electricity Usage** (total units consumed).
   - **Charge Per Unit** of electricity.

2. **Calculate**: Press the **Calculate** button to view the total per person.
3. **Export to PDF**: Press **Print** to save results as a PDF file at `~/Desktop/mini project/task/roomrent` (ensure this directory exists or update the path as needed in the code).
4. **Exit**: Close the app by clicking the **Exit** button.

## 📝 PDF Output

- A PDF named `RoomRentCalculation.pdf` will be generated with details:
  - Total Rent
  - Total Food Expenses
  - Total Electricity Bill
  - Total Amount Per Person
- The file will be saved to `~/Desktop/mini project/task/roomrent` (adjust the path in the code if necessary).

## 🔍 Example Calculation

For example, with:
- **Rent**: 2000
- **Food Expenses**: 500
- **Electricity Usage**: 100 units at a **Charge per Unit** of 5

The calculation is:
1. **Electricity Bill** = 100 * 5 = 500
2. **Total Expense** = 2000 (rent) + 500 (food) + 500 (electricity) = 3000
3. **Per Person Amount** (if 3 people) = 3000 / 3 = 1000

The result will display in the GUI and can be saved as a PDF.

## ⚠️ Troubleshooting
- **Input Error**: If you see an "Input Error," check that all fields have valid numeric values.
- **PDF Save Error**: Ensure the output directory exists or update the path in the code.

## 📜 License
This project is licensed under the MIT License.

---

### 🎉 Happy Calculating!
This Room Rent Calculator makes sharing expenses among roommates easier and provides convenient PDF documentation.
```

This version is structured to be more visually organized and user-friendly for GitHub’s `README.md` file format, making it easy to understand the application’s purpose, setup, and usage instructions.

import tkinter as tk
from tkinter import messagebox
import os
from fpdf import FPDF

def calculate_total():
    try:
        totalperson = int(entry_totalperson.get())
        rent = int(entry_rent.get())
        food = int(entry_food.get())
        eletricity = int(entry_eletricity.get())
        charge = int(entry_charge.get())

        totalbill = eletricity * charge
        total = (rent + food + totalbill) // totalperson

        messagebox.showinfo("Result", f"Total amount should be paid by each person is: {total}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Room Rent Calculator")

tk.Label(root, text="Enter the total number of person:").grid(row=0, column=0)
entry_totalperson = tk.Entry(root)
entry_totalperson.grid(row=0, column=1)

tk.Label(root, text="Enter the total rent:").grid(row=1, column=0)
entry_rent = tk.Entry(root)
entry_rent.grid(row=1, column=1)

tk.Label(root, text="Enter the total food order:").grid(row=2, column=0)
entry_food = tk.Entry(root)
entry_food.grid(row=2, column=1)

tk.Label(root, text="Enter the eletricity bill spends:").grid(row=3, column=0)
entry_eletricity = tk.Entry(root)
entry_eletricity.grid(row=3, column=1)

tk.Label(root, text="Enter the charge per unit:").grid(row=4, column=0)
entry_charge = tk.Entry(root)
entry_charge.grid(row=4, column=1)

tk.Button(root, text="Exit", command=root.quit).grid(row=5, column=1)

def print_total():
    try:
        totalperson = int(entry_totalperson.get())
        rent = int(entry_rent.get())
        food = int(entry_food.get())
        eletricity = int(entry_eletricity.get())
        charge = int(entry_charge.get())

        totalbill = eletricity * charge
        total = (rent + food + totalbill) // totalperson

        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Room Rent Calculation", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Total Rent: {rent}", ln=True)
        pdf.cell(200, 10, txt=f"Total Food: {food}", ln=True)
        pdf.cell(200, 10, txt=f"Total Electricity Bill: {totalbill}", ln=True)
        pdf.cell(200, 10, txt=f"Total Amount per Person: {total}", ln=True)

        # Save the PDF
        pdf_output_path = os.path.join(os.path.expanduser("~"), "Desktop/mini project/task/roomrent", "RoomRentCalculation.pdf")
        pdf.output(pdf_output_path)

        messagebox.showinfo("Result", f"PDF created successfully at {pdf_output_path}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

tk.Button(root, text="Print", command=print_total).grid(row=5, column=0)

tk.Button(root, text="Calculate", command=calculate_total).grid(row=5, column=0, columnspan=2)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Multiplication App")
root.geometry("350x250")
root.configure(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="Multiply Two Numbers", 
                       font=("Arial", 14, "bold"), bg="lightblue")
title_label.pack(pady=10)

# First Number
tk.Label(root, text="Enter First Number:", bg="lightblue").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Second Number
tk.Label(root, text="Enter Second Number:", bg="lightblue").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Calculate Button
calc_button = tk.Button(root, text="Calculate Product", 
                        command=calculate_product, bg="green", fg="white")
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Product: ", 
                        font=("Arial", 12), bg="lightblue")
result_label.pack(pady=5)

# Run application
root.mainloop()
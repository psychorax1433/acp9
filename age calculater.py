import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime

# ── helper: calculate age ───────────────────────────────────────────────────────
def calculate_age(birth_date: date) -> int:
    today = date.today()
    years = today.year - birth_date.year
    # If birthday hasn’t occurred yet this year, subtract 1
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years

# ── callback for the button ────────────────────────────────────────────────────
def on_calculate():
    try:
        d = int(day_var.get())
        m = int(month_var.get())
        y = int(year_var.get())
        birth = date(y, m, d)                # raises ValueError if invalid
        age = calculate_age(birth)
        result_var.set(f"Age: {age} years")
    except ValueError:
        messagebox.showerror("Invalid date",
                             "Please enter a valid numeric date (DD MM YYYY).")

# ── GUI setup ──────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Age Calculator")

# Labels & entries
tk.Label(root, text="Day (DD):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Month (MM):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Year (YYYY):").grid(row=2, column=0, padx=5, pady=5, sticky="e")

day_var   = tk.StringVar()
month_var = tk.StringVar()
year_var  = tk.StringVar()
result_var = tk.StringVar()

tk.Entry(root, textvariable=day_var,   width=8).grid(row=0, column=1, padx=5, pady=5)
tk.Entry(root, textvariable=month_var, width=8).grid(row=1, column=1, padx=5, pady=5)
tk.Entry(root, textvariable=year_var,  width=8).grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate Age", command=on_calculate).grid(
    row=3, column=0, columnspan=2, pady=10
)

tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold")).grid(
    row=4, column=0, columnspan=2, pady=5
)

root.mainloop()

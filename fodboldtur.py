import tkinter as tk
from tkinter import messagebox, ttk
import pickle

filename = 'betalinger.pk'
goal_amount = 4500.0

try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
except (FileNotFoundError, EOFError):
    fodboldtur = {}

names = list(fodboldtur.keys())

root = tk.Tk()
root.title("Fodboldtur Payment")

def save_data():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)

def alert(message):
    messagebox.showerror("Error", message)

def build_progress_bars():
    for widget in progress_frame.winfo_children():
        widget.destroy()
    sorted_names = sorted(fodboldtur.keys(), key=lambda n: fodboldtur[n], reverse=True)
    for name in sorted_names:
        frame = tk.Frame(progress_frame)
        frame.pack(fill="x", pady=3)
        label = tk.Label(frame, text=name, width=20, anchor="w")
        label.pack(side="left")
        progress = ttk.Progressbar(frame, length=200, mode='determinate', maximum=goal_amount)
        progress.pack(side="left", padx=5)
        progress['value'] = fodboldtur.get(name, 0)
        amount_label = tk.Label(frame, text=f"{fodboldtur.get(name, 0):.2f} / {goal_amount:.0f} DKK")
        amount_label.pack(side="left")
        progress_bars[name] = (progress, amount_label)

def reset_file():
    if not fodboldtur:
        alert("No data to reset.")
        return
    confirm = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all payments to 0 DKK?")
    if confirm:
        for name in fodboldtur.keys():
            fodboldtur[name] = 0.0
        save_data()
        build_progress_bars()
        messagebox.showinfo("Reset Complete", "All payments have been reset to 0 DKK.")

def pay():
    name = combo_box.get()
    amount_text = e1.get().strip()
    if name not in names:
        alert("Please select a valid person.")
        return
    try:
        amount = float(amount_text)
    except ValueError:
        alert("Please enter a valid number.")
        return
    if amount <= 0:
        alert("Amount must be greater than zero.")
        return
    current = fodboldtur.get(name, 0.0)
    if current + amount > goal_amount:
        alert(f"Payment would exceed 4500 DKK for {name}. Current: {current:.2f} DKK.")
        return
    fodboldtur[name] = current + amount
    save_data()
    build_progress_bars()
    messagebox.showinfo("Payment Registered", f"{name} has paid {amount:.2f} DKK!")
    e1.delete(0, tk.END)
    combo_box.set("Select a name")

main_frame = tk.Frame(root)
main_frame.pack(padx=15, pady=15)

tk.Label(main_frame, text="Selected Person:").pack(pady=5)
combo_box = ttk.Combobox(main_frame, values=names, state='readonly')
combo_box.pack(pady=5)
combo_box.set("Select a name")

tk.Label(main_frame, text="Amount (DKK):").pack(pady=5)
e1 = tk.Entry(main_frame)
e1.pack(pady=5)

button = tk.Button(main_frame, text="Register Payment", width=25, command=pay)
button.pack(pady=10)

progress_frame = tk.LabelFrame(root, text="Payment Progress", padx=10, pady=10)
progress_frame.pack(padx=15, pady=10, fill="x")

progress_bars = {}
build_progress_bars()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset Payments", command=reset_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
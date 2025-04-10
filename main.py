import tkinter as tk

# --- Original GUI interface code (commented out) ---
# root = tk.Tk()
# root.title("Simple GUI")
# root.mainloop()

# --- Modified GUI with all requirements ---
def toggle_button_color(button):
    current_color = button["bg"]
    new_color = "lightgreen" if current_color == "lightcoral" else "lightcoral"
    button.config(bg=new_color)

root = tk.Tk()
root.title("Easter Homework GUI")
root.geometry("400x300")
root.configure(bg="lightblue")  # Background for the whole window

# 1) Labels
label1 = tk.Label(root, text="Enter your name:", bg="lavender")
label1.pack(pady=5)

# 2) Text Boxes
entry1 = tk.Entry(root, bg="white")
entry1.pack(pady=5)

# 3) Switch Buttons (change color on click)
button_short = tk.Button(root, text="Short Switch", bg="lightcoral", command=lambda: toggle_button_color(button_short))
button_short.pack(pady=5)

button_long = tk.Button(root, text="Long Switch", bg="lightcoral", command=lambda: toggle_button_color(button_long))
button_long.pack(pady=5)

# 4) Check Boxes
check_var1 = tk.IntVar()
check1 = tk.Checkbutton(root, text="Option A", variable=check_var1, bg="lightyellow")
check1.pack(pady=5)

check_var2 = tk.IntVar()
check2 = tk.Checkbutton(root, text="Option B", variable=check_var2, bg="lightyellow")
check2.pack(pady=5)

root.mainloop()

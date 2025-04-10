import tkinter as tk

def display_name():
    name = entry.get() #Getting input
    if name=="":
        output_label.config(text="Please enter a name")
    else:
        output_label.config(text=f"Hello, {name}!") #Output to a label

root = tk.Tk()
root.title("my ui teehee")
root.geometry("600x500")
root.configure(bg="lightblue")

label1 = tk.Label(root, text="Enter name here: ", foreground="red")
label1.pack(pady=5)
# Entry (Text box for input)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button
submit_btn = tk.Button(root, text="Submit", command=display_name)
submit_btn.pack(pady=5)

# Label (Output)
output_label = tk.Label(root, text="", foreground="black", background="lightblue", font=("Comic Sans MS", 16, "bold"))
output_label.pack(pady=10)

def toggle(): #For switch
    if switch["text"] == "OFF":
        switch.config(text="ON", bg="lightgreen")
        print("button is on")
    else:
        switch.config(text="OFF", bg="lightcoral")
        print("button is off")

switch = tk.Button(root, text="OFF", width=10, bg="lightcoral", command=toggle)
switch.pack(pady=20)

label2 = tk.Label(root, text="Is Tracey awesome?:", background="yellow")
label2.pack()

def show_state():
    if choice.get() == "Yes":
        label3.config(text="yeahhh i am!!", background="pink")
    else:
        label3.config(text="i think u miss clicked", background="pink")

choice = tk.StringVar(value=None)  # Default is "No"

# Radio Buttons
checkYes = tk.Radiobutton(root, text="Yes", variable=choice, value="Yes", command=show_state, foreground="orange", background="purple", width=10)
checkYes.pack()

checkNo = tk.Radiobutton(root, text="No", variable=choice, value="No", command=show_state, foreground="orange", background="purple", width=10)
checkNo.pack()

label3 = tk.Label(root, text="", background="lightblue", width=20, height=2)
label3.pack(pady=5)

root.mainloop()

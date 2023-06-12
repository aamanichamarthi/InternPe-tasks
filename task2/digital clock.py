import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label for displaying the time
time_label = tk.Label(window, font=('Times New Roman', 80), bg='white', fg='black')
time_label.pack(pady=50)

# Start the clock
update_time()

# Run the main window's event loop
window.mainloop()

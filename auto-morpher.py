import tkinter as tk
from tkinter import ttk
import pyautogui
import pyperclip
import keyboard
import time
import pydirectinput


# Function that runs when the "Execute" button is pressed


def execute_action():
    # 3-second countdown
    for i in range(3, 0, -1):
        countdown_label.insert('1.0', f"Starting in {i} seconds...")
        root.update()
        time.sleep(1)

    #countdown_label.delete('1.0', )
    countdown_label.insert('end', "Executing...")
    root.update()

    # read and process text from box
    text = textbox.get("1.0", tk.END)
    speed = float(speedbox.get("1.0", "end-1c")) if speedbox.get("1.0", "end-1c") else .85
    lines = text.strip().split("\n")
    print(lines)

    # Check if the checkbox is enabled
    Bottomdec2 = int(var2.get())

    time.sleep(0.8)

    for line in lines:
        line = line.replace(":", "")

        # Opening command Bar
        pydirectinput.press("'")


        pyperclip.copy(line)

        # Writes the line to be sent
        pyautogui.hotkey('ctrl', 'v')

        # Press Enter
        pydirectinput.press("enter")

        if Bottomdec2 == 1:
            # Checking if the refresh command is in the line
            if "ref" in line:
                time.sleep(3)

        # Short pause between lines
        time.sleep(speed)

    # Done
    countdown_label.insert('end', "Morphing Finished")
    pyperclip.copy('')

# Create main window
root = tk.Tk()
root.title("Auto Morpher")
root.geometry("450x500")
root.configure(bg="#f0f0f0")

# Use ttk for modern styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TCheckbutton", font=("Segoe UI", 10))
style.configure("TLabel", font=("Segoe UI", 10))

# Frame for layout
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# Add textbox label and box
ttk.Label(frame, text="Input Text:").pack(anchor="w", pady=(0, 5))
textbox = tk.Text(frame, height=10, width=50, font=("Consolas", 10))
textbox.pack(pady=(0, 15))

# Speed label and entry
ttk.Label(frame, text="Delay between lines (seconds):").pack(anchor="w")
speedbox = tk.Text(frame, height=1, width=10, font=("Segoe UI", 10))
speedbox.pack(pady=(0, 15))

# Add checkbox, optional functionality
var2 = tk.IntVar()
c2 = ttk.Checkbutton(frame, text='Enable Refresh Wait', variable=var2, onvalue=1, offvalue=0)
c2.pack(pady=(0, 15))

# Add button
execute_button = ttk.Button(frame, text="Execute", command=execute_action)
execute_button.pack(pady=(0, 20))

# Add Countdown Label
ttk.Label(frame, text="Status:").pack(anchor="w")
countdown_label = tk.Text(frame, height=4, width=50, font=("Segoe UI", 9), bg="#e6e6e6")
countdown_label.pack()

# Open window
root.mainloop()

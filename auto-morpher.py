import tkinter as tk
import pyautogui
import pyperclip
import keyboard
import time
import pydirectinput


# Function that runs when the "Execute" button is pressed


def execute_action():
    # 3-second countdown
    for i in range(3, 0, -1):
        countdown_label.insert('1.0', "Starting in {i} seconds...")
        root.update()
        time.sleep(1)

    #countdown_label.delete('1.0', )
    countdown_label.insert('end', "Executing...")
    root.update()

    # read and process text from box
    text = textbox.get("1.0", tk.END)
    speed = float(speedbox.get("1.0", "end-1c")) if speedbox.get("1.0", "end-1c") else 1
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
root.geometry("400x400")

# Add textbox
textbox = tk.Text(root, height=10, width=40)
textbox.pack(pady=20)

# Add speed box
speedbox = tk.Text(root, height=1, width=5)
speedbox.pack(pady=5)

# Add button
execute_button = tk.Button(root, text="Execute", command=execute_action)
execute_button.pack(pady=5)

# Add checkbox, optional functionality
var2 = tk.IntVar()
c2 = tk.Checkbutton(root, text='Enable Refresh wait.', variable=var2, onvalue=1, offvalue=0)
c2.pack(pady=5)

#Add Countdown Label
countdown_label = tk.Text(root)

# Opens Window
root.mainloop()
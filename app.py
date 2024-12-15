import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def reset_text():
    text_entry.delete("1.0", tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Text-to-Speech")
root.geometry("400x300")

header = tk.Label(root, text="Text-to-Speech", font="Times 20 bold", fg="brown")
header.pack(pady=10)

sub_header = tk.Label(root, text="Enter your text:", font="Times 16", fg="brown")
sub_header.pack(pady=10)

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", font="bold", bg="green", fg="white", width=8, command=play_text)
play_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", font="bold", bg="blue", fg="white", width=8, command=reset_text)
reset_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Exit", font="bold", bg="red", fg="white", width=8, command=exit_app)
exit_button.grid(row=0, column=2, padx=5)

root.mainloop()
""" Click Kanye for quotes """
from tkinter import Tk, Canvas, PhotoImage, Button
import os
import requests


def get_quote():
    """ API call to retrieve quote """
    try:
        quote = requests.get("https://api.kanye.rest", timeout=10)
        quote.raise_for_status()
    except requests.exceptions.Timeout:
        print("Timed out")
    new_text = quote.json()
    canvas.itemconfig(quote_text, text=new_text["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#f7f5dd")

# Get current folder path
current_dir = os.path.dirname(__file__)
bg_path = os.path.join(current_dir, "background.png")
kanye_path = os.path.join(current_dir, "kanye.png")

canvas = Canvas(width=300, height=414, bg="#f7f5dd", highlightthickness=0)
background_img = PhotoImage(file=bg_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207,
    text="Click Kanye for Quotes",
    width=250,
    font=("Arial", 18, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=kanye_path)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()

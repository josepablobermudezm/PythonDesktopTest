
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")


canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    618.0,
    162.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_1.place(
    x=491.0,
    y=139.0,
    width=254.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    618.0,
    245.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_2.place(
    x=491.0,
    y=222.0,
    width=254.0,
    height=44.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    618.0,
    324.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_3.place(
    x=491.0,
    y=301.0,
    width=254.0,
    height=44.0
)

canvas.create_text(
    40.0,
    127.0,
    anchor="nw",
    text="Welcome to Tkinter Designer",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    40.0,
    160.0,
    100.0,
    165.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    40.0,
    191.0,
    anchor="nw",
    text="Tkinter Designer uses Figma API to",
    fill="#FCFCFC",
    font=("AdobeArabic Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    217.0,
    anchor="nw",
    text="analyse the design file and creates the",
    fill="#FCFCFC",
    font=("AdobeArabic Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    243.0,
    anchor="nw",
    text="respective code and files needed for the GUI.",
    fill="#FCFCFC",
    font=("AdobeArabic Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    269.0,
    anchor="nw",
    text="Even Tkinter Designer's GUI is created using Tkinter Designer.",
    fill="#FCFCFC",
    font=("AdobeArabic Regular", 24 * -1)
)

canvas.create_text(
    482.0,
    68.0,
    anchor="nw",
    text="Enter the details.",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    492.0,
    143.0,
    anchor="nw",
    text="Token ID",
    fill="#505485",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    492.0,
    227.0,
    anchor="nw",
    text="File URL",
    fill="#505485",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    492.0,
    308.0,
    anchor="nw",
    text="Output Path",
    fill="#505485",
    font=("Arial BoldMT", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=545.0,
    y=387.0,
    width=146.0,
    height=36.0
)
window.resizable(False, False)
window.mainloop()

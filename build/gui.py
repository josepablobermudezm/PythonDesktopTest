from pathlib import Path
# from tkinter import *
from tkinter import ttk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")

def selection_changed(event):
    tipoExcibicion.set('')
    if combo.get() == "DPP":
        tipoExcibicion["values"] = ["Cabecera", "Lateral de Pie"]
    else:
        tipoExcibicion['values'] = ('Cabecera', 'Lateral de Pie', 'Lateral Colgante', 'Isla')

canvas = Canvas(
    window,
    bg = "#ffffff",
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
    fill="#3A7FF6",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    167.0,
    162.0,
    image=entry_image_1
)

# Define the style for combobox widget
style= ttk.Style()
style.theme_use('xpnative')
style.configure("TCombobox")

combo = ttk.Combobox(window)
combo['values'] = (
    'DPP', 'HSM')
combo.set('HSM')
combo.state(['readonly'])
combo.place(
    x=40.0,
    y=160.0,
    width=254.0,
    height=20.0
)
combo.bind("<<ComboboxSelected>>", selection_changed)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    167.0,
    245.0,
    image=entry_image_2
)
"""
entry_2 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_2.place(
    x=40.0,
    y=243.0,
    width=254.0,
    height=25.0
)
"""


tipoExcibicion = ttk.Combobox(window)
tipoExcibicion['values'] = (
    'Cabecera', 'Lateral de Pie', 'Lateral Colgante', 'Isla')
tipoExcibicion.state(['readonly'])
tipoExcibicion.place(
    x=40.0,
    y=243.0,
    width=254.0,
    height=20.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    167.0,
    324.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_3.place(
    x=40.0,
    y=322.0,
    width=254.0,
    height=25.0
)

canvas.create_text(
    31.0,
    68.0,
    anchor="nw",
    text="Enter the details.",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    41.0,
    143.0,
    anchor="nw",
    text="Canal",
    fill="#505485",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    41.0,
    227.0,
    anchor="nw",
    text="Tipo de Exhibición",
    fill="#505485",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    41.0,
    308.0,
    anchor="nw",
    text="Cantidad Locales",
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
    x=94.0,
    y=387.0,
    width=146.0,
    height=36.0
)

lst = [("EAN", 'Descripción Del Producto', "FULL FACING"),
       (7500435157568, 'PACK PANTENE SH.REST.X400ML+3M', 19),
       (7500435157551, 'PACK PANTENE REST.SH.X400+AC.X', 18),
       (7500435134699, 'PANTENE MICELAR SH.400+AC.', 20),
       (7500435186339, 'Pack Pantene Bambú', 21),
       (7500435020008, 'HYS SH.LIMPIEZA RENOVADORA X37', 21),
       (7500435138000, 'HYS SH.CHARCOAL X375ML',  21),
       (7500435159210, 'HS SH Fuerza de raiz 375MLX12IT',21)]

# total number of rows and columns in list
total_rows = len(lst)
total_columns = len(lst[0])

for i in range(total_rows):
    for j in range(total_columns):
        e = Entry(window, width=15, fg='black',
                       font=('Arial BoldMT', 10))
        #e.grid(row=i, column=j)
        e.place(
            x=450.0+(j*133),
            y=100.0+(i*50),
            width=130.0,
            height=36.0
        )
        e.insert(0, lst[i][j])

window.resizable(False, False)
window.mainloop()

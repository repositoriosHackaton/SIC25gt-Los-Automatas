import tkinter as tk 
from interfaz import abririInterfazInicio
from tkinter import *
from PIL import Image, ImageTk


def abrirInterfaz():
    app.destroy()
    abririInterfazInicio()
    print("-"*50)
    print("Se abrio la interfaz principal 1")
    print("-"*50)


#! Ventana
app = tk.Tk()
# app.overrideredirect(True)


app.title("Bienvenida!")
app.geometry('650x300')

app.iconbitmap("img\icono.ico")

#? Dimensiones de la pantalla para centrar
wtotal = app.winfo_screenwidth()
print(wtotal)
htotal = app.winfo_screenheight()
print(htotal)
wventana = 650
hventana = 300
x = round(wtotal/2 - wventana/2)
y = round(htotal/2 - hventana/2)


#* Configuramos ventana
app.configure(bg='DarkOrchid4')
app.geometry(str(wventana)+"x"+str(hventana)+"+"+str(x)+"+"+str(y))


#* Agregamos Labels y botones
labelTitulo1 = tk.Label(
    app, 
    text="Recon de Neumonia", 
    font=("Arial", 36, "bold"), 
    fg='white', 
    bg='DarkOrchid4')
labelTitulo1.pack(pady=20)

labelBienvenida = tk.Label(
    app, 
    text="Bienvenido usuario", 
    font=("Arial", 15, "bold"), 
    fg='white', 
    bg='DarkOrchid4')

labelBienvenida.pack(pady=20)

botonIniciar = tk.Button(
    app, 
    text="Iniciar", 
    font=("Arial", 12, "bold"), 
    cursor="hand2",
    fg='white', bg='gray10', 
    height= 2,
    # width= 20,
    command=abrirInterfaz)
botonIniciar.pack(pady=20)


app.mainloop()
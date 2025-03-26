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

app.iconbitmap("ProjectHackathon\SIC25gt-Los-Automatas\src\img\icono.ico")

#* Cambiar title Bar, si se quiere regresar a normal quitar esto, 
# titleBar = Frame(app, bg='black', relief='raised', bd=4, highlightthickness=0)
# close_button = Button(titleBar, text='X', command= app.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 1,font="bold",fg='white',highlightthickness=0)
# window = Canvas(app, bg='black', highlightthickness=0)
# titleBar.pack(expand=1, fill=X)
# close_button.pack(side=RIGHT)
# window.pack(expand=1, fill=BOTH)

# xwin=None
# ywin=None

# def move_window(event):
#     app.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
# def change_on_hovering(event):
#     global close_button
#     close_button['bg']='red'
# def return_to_normalstate(event):
#     global close_button
#     close_button['bg']='#2e2e2e'
    

# titleBar.bind('<B1-Motion>', move_window)
# close_button.bind('<Enter>',change_on_hovering)
# close_button.bind('<Leave>',return_to_normalstate)

#* Termina title bar

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
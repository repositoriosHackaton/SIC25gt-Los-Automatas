import tkinter as tk 

def abririInterfazInicio():

    print('-'*50)
    print("Se abrio la interfaz principal 2")
    print('-'*50)

    app = tk.Tk()

    #* Iniciamos ventana
    app.title("Interfaz de prueba")
    app.geometry('800x600')


    #? Dimensiones de la pantalla para centrar
    wtotal = app.winfo_screenwidth()
    print(wtotal)
    htotal = app.winfo_screenheight()
    print(htotal)
    wventana = 800
    hventana = 600
    x = round(wtotal/2 - wventana/2)
    y = round(htotal/2 - hventana/2)


    #* Configuramos ventana
    app.configure(bg='DarkOrchid4')
    app.geometry(str(wventana)+"x"+str(hventana)+"+"+str(x)+"+"+str(y))

    # geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


    #* Agregamos Labels y botones
    labelTitulo1 = tk.Label(
        app, 
        text="Reconocimiento de Neumonia", 
        font=("Arial", 36, "bold"), 
        fg='white', 
        bg='DarkOrchid4')
    labelTitulo1.pack(pady=20)

    labelCarga1 = tk.Label(
        app,
        text="Cargue la imagen que desea analizar",
        font=("Arial", 15, "bold"),
        fg='white',
        bg='DarkOrchid4'
    )
    labelCarga1.pack(pady=30)

    butonCargar = tk.Button (
        app, 
        text="Cargar imagen de pulmones",
        font=("Arial", 12, "bold"),
        bg='white',
        fg='black',
        
    )
    butonCargar.pack(pady=20)


    app.mainloop()


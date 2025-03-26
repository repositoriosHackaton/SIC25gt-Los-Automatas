import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk

imagenCargada = None

def abririInterfazInicio():


    def cargarImagen():
        global imagenCargada
        print("Cargando imagen")

        try:
            archivo = filedialog.askopenfilename(
                title="Seleccione una imagen", 
                filetypes=[("Imagenes", "*.png *.jpg *.jpeg")])
            
            if archivo:
                print("Se cargo la imagen")
                img = Image.open(archivo)
                img2 = img.resize((350, 300))
                imagen2 = ImageTk.PhotoImage(img2)
                imagenCargada = ImageTk.PhotoImage(img)

                etiquetaImagen = tk.Label(image=imagenCargada)
                etiquetaImagen.image = imagenCargada

                output = tk.Label(app, text=archivo, image=imagen2)
                output.image = imagen2
                output.pack()
        
        except Exception as e:
            print(e)
            print("Error al cargar la imagen")

    def analizarImg():
        print("Analizando imagen")
        #? hacer logica para llamar a los metodos q analizan la imagen desde main.py


    app = tk.Tk()

    #* Iniciamos ventana
    app.title("Reconocimiento de Neumonia")
    app.geometry('800x600')

    app.iconbitmap("ProjectHackathon\SIC25gt-Los-Automatas\src\img\icono.ico")



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
        text="Cargue la imagen que desea analizar:",
        font=("Arial", 15, "bold"),
        fg='white',
        bg='DarkOrchid4'
    )
    labelCarga1.pack(pady=10)

    butonCargar = tk.Button (
        app, 
        text="Cargar imagen de pulmones",
        font=("Arial", 12, "bold"),
        bg='white',
        fg='black',
        command=cargarImagen
    )
    butonCargar.pack(pady=10)

    butonAnalizar = tk.Button (
        app, 
        text="Analizar imagen",
        font=("Arial", 12, "bold"),
        bg='white',
        fg='black',
        command=analizarImg
    )
    butonAnalizar.pack(pady=20)

    #? Hacer logica para que aparezca la imagen cargada


    app.mainloop()


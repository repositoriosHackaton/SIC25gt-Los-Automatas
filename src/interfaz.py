import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk

imagenCargada = None
imagenRedimensionada = None
rutaImagen = None

def abririInterfaz():


    def cargarImagen():
        global imagenCargada, imagenRedimensionada, rutaImagen
        print("Cargando imagen")

        try:
            archivo = filedialog.askopenfilename(
                title="Seleccione una imagen", 
                filetypes=[("Imagenes", "*.png *.jpg *.jpeg")])
            
            if archivo:
                print("Se cargo la imagen")
                rutaImagen = archivo
                # img = Image.open(archivo)
                
                # imagenCargada = img

                # imgRedimensionada = img.resize((300, 300))
                # imagenRedimensionada = ImageTk.PhotoImage(imgRedimensionada)

                # if 'etiquetaImagen' in globals() and etiquetaImagen is not None:
                #     etiquetaImagen.destroy()

                # etiquetaImagen = tk.Label(app, image=imagenRedimensionada)
                # etiquetaImagen.image = imagenRedimensionada  # Mantener la referencia
                # etiquetaImagen.pack(pady=10)
            
        except Exception as e:
            print(e)
            print("Error al cargar la imagen")

    def analizarImagen():
        global rutaImagen
        try:
            if rutaImagen:        
                print("Analizando imagen")
                #? hacer logica para llamar a los metodos q analizan la imagen desde main.py
                from main import analizarImg  # Importar aquí para evitar el ciclo

                resultado, porcentajePrediccionStr = analizarImg(rutaImagen)
                etiquetaResultado.config(
                    text=f"Resultado: {resultado}\nConfianza: {porcentajePrediccionStr}"
                )
            else:
                tk.messagebox.showwarning(title="Advertencia", message="Primero debe de seleccionar una imagen.", )
        except Exception as e:
            print(e)
            print("Error al analizar la imagen")

    def cerraVentana():
        print("Terminando programa...")
        app.destroy()
        exit()

    app = tk.Tk()

    #* Iniciamos ventana
    app.title("Reconocimiento de Neumonia")
    app.geometry('800x600')

    app.iconbitmap("img\icono.ico")



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
    app.protocol("WM_DELETE_WINDOW", cerraVentana)

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
        command=analizarImagen
    )
    butonAnalizar.pack(pady=20)

    etiquetaResultado = tk.Label(
        app,
        text="",
        font=("Arial", 15, "bold"),
        fg='white',
        bg='DarkOrchid4'
    )
    etiquetaResultado.pack(pady=20)

    #? Hacer logica para que aparezca la imagen cargada


    app.mainloop()


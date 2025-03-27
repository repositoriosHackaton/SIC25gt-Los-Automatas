import tkinter as tk

def ventanaInformacionNeumonia():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Información sobre la Neumonía")
    ventana.geometry("600x400")
    ventana.configure(bg="DarkOrchid4")

    # Título
    titulo = tk.Label(
        ventana,
        text="¿Qué es la Neumonía?",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="DarkOrchid4"
    )
    titulo.pack(pady=10)

    # Texto explicativo
    texto = (
        "La neumonía es una infección que inflama los sacos de aire de uno o ambos pulmones. "
        "Los sacos de aire pueden llenarse de líquido o pus, causando síntomas como tos, fiebre, "
        "escalofríos y dificultad para respirar. Puede ser causada por bacterias, virus u hongos.\n\n"
        "Es importante buscar atención médica si se presentan síntomas graves, especialmente en "
        "niños pequeños, adultos mayores o personas con sistemas inmunitarios debilitados."
    )

    etiquetaTexto = tk.Label(
        ventana,
        text=texto,
        font=("Arial", 12),
        fg="white",
        bg="DarkOrchid4",
        wraplength=550,  # Ajustar el texto para que no se salga de la ventana
        justify="left"
    )
    etiquetaTexto.pack(pady=20)

    # Botón para cerrar la ventana
    botonCerrar = tk.Button(
        ventana,
        text="Cerrar",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="black",
        command=ventana.destroy
    )
    botonCerrar.pack(pady=10)

    # Ejecutar la ventana
    ventana.mainloop()


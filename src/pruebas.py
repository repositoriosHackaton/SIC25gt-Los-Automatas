import tkinter as tk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import ctypes as ct

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Diabetic Retinopathy Detection")
        self.image = ""

        window_width = 700
        window_height = 550
        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Apply dark title bar
        self.dark_title_bar(self.root)

        file_upload = tk.Button(self.root, text="Upload 2D Fundus Image",
                                command=lambda: self.upload_file())
        file_upload.pack()

        self.root.resizable(False, False)

    def run(self):
        self.root.mainloop()

    def upload_file(self):
        file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg *jpg *png')])
        if file_path is not None:
            pass
        img = ImageTk.PhotoImage(Image.open(file_path.name))
        self.image = img

        output = tk.Label(self.root, text=file_path.name, image=self.image)
        output.pack()

    def dark_title_bar(self, window):
        """
        MORE INFO:
        https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        """
        try:
            window.update()
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
            get_parent = ct.windll.user32.GetParent
            hwnd = get_parent(window.winfo_id())
            rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
            value = 1  # 2 para modo oscuro, 0 para desactivarlo
            value = ct.c_int(value)
            set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
            print("Modo oscuro aplicado a la barra de título.")
        except Exception as e:
            print(f"Error al aplicar el modo oscuro: {e}")

try:
    ct.windll.dwmapi
    print("dwmapi.dll está disponible.")
except AttributeError:
    print("dwmapi.dll no está disponible.")
new_app = App()
new_app.run()
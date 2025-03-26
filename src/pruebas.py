import tkinter as tk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


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
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        file_upload = tk.Button(self.root, text="Upload 2D Fundus Image",
                                command=lambda: self.upload_file())
        file_upload.pack()

        self.root.resizable(False, False)

        # when loading a file in, root.lower()

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


new_app = App()
new_app.run()
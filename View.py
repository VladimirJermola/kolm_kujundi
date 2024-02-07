from tkinter import *
import tkinter.font as font



class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 550
        self.__height = 300
        self.default_font = font.Font(family="Verdana", size=14)

        self.title("Silindri Gui")
        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        self.lbl_radius, self.lbl_height, self.radius_entry, self.height_entry, self.btn_arvuta, self.text_box = self.create_frame_widgets()

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, bg="blue", height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg="yellow")
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        lbl_radius = Label(self.top_frame, text="Sisesta raadius", font=self.default_font)
        lbl_radius.grid(row=0, column=0, padx=5, pady=5)
        lbl_height = Label(self.top_frame, text="Sisesta kõrgus", font=self.default_font)
        lbl_height.grid(row=1, column=0, padx=5, pady=5)
        radius_entry = Entry(self.top_frame, font=self.default_font)
        radius_entry.grid(row=0, column=1, padx=5, pady=5)
        radius_entry.focus()
        height_entry = Entry(self.top_frame, font=self.default_font)
        height_entry.grid(row=1, column=1, padx=5, pady=5)
        btn_arvuta = Button(self.top_frame, text="Arvuta", font=self.default_font, command=self.controller.arvuta_click)
        btn_arvuta.grid(row=1, column=3, padx=5, pady=5, sticky="EW")
        text_box = Text(self.bottom_frame, font=self.default_font, state=DISABLED)
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)
        return lbl_radius, lbl_height, radius_entry, height_entry, btn_arvuta, text_box  #, num_entry, btn_send, text_box, btn_scoreboard


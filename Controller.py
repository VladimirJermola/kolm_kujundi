from math import pi
from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)




    def arvuta_click(self):
        radius = self.model.get_user_input_radius(self.view.radius_entry.get().strip())
        height = self.model.get_user_input_height(self.view.height_entry.get().strip())
        volume = pi * float(self.view.radius_entry.get().strip()) ** 2 * float(self.view.height_entry.get().strip())
        base_surface = pi * float(self.view.radius_entry.get().strip()) ** 2
        lateral_surface = 2 * pi * float(self.view.radius_entry.get().strip()) * float(self.view.height_entry.get().strip())
        self.view.text_box.config(state="normal")
        self.view.text_box.insert("insert", "Raadius: " + str(self.model.cylinder.radius) + "\n")
        self.view.text_box.insert("insert", "Kõrgus: " + str(self.model.cylinder.height) + "\n") # kirjuta tulemus kasti
        self.view.text_box.insert("insert", "Ruumala: " + str(volume) + "\n")
        self.view.text_box.insert("insert", "Põhja pindala: " + str(base_surface) + "\n")
        self.view.text_box.insert("insert", "Külje pindala: " + str(lateral_surface) + "\n")
        self.view.text_box.see("end")
        self.view.text_box.config(state="disabled")
        self.view.btn_arvuta.config(state="disabled")









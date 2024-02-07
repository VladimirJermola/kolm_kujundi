from math import pi
from  Model3 import Model
from View3 import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)




    def arvuta_click(self):
        radius = self.model.get_user_input_radius(self.view.radius_entry.get().strip())
        kulg = self.model.get_user_input_height(self.view.height_entry.get().strip())
        pindala_ilma_otsteta = 2 * float(self.view.radius_entry.get().strip()) * float(self.view.height_entry.get().strip())
        umbermoot = 2 * (pi *float(self.view.radius_entry.get().strip()) + float(self.view.height_entry.get().strip()))
        pindala = pi * float(self.view.radius_entry.get().strip()) ** 2 + 2 * float(self.view.radius_entry.get().strip()) * float(self.view.height_entry.get().strip())
        self.view.text_box.config(state="normal")
        self.view.text_box.insert("insert", "Raadius: " + str(self.model.cylinder.radius) + "\n")
        self.view.text_box.insert("insert", "Külg: " + str(self.model.cylinder.height) + "\n") # kirjuta tulemus kasti
        self.view.text_box.insert("insert", "Pindala ilma otsteta: " + str(pindala_ilma_otsteta) + "\n")
        self.view.text_box.insert("insert", "Ümbermõõt: " + str(umbermoot) + "\n")
        self.view.text_box.insert("insert", "Pindala: " + str(pindala) + "\n")
        self.view.text_box.see("end")
        self.view.text_box.config(state="disabled")
        self.view.btn_arvuta.config(state="disabled")









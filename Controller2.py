from math import pi, sqrt
from Model2 import Model
from View2 import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)




    def arvuta_click(self):
        kulg = self.model.get_user_input_radius(self.view.radius_entry.get().strip())
        kulg2 = self.model.get_user_input_height(self.view.height_entry.get().strip())
        diagonaal = sqrt(float(self.view.radius_entry.get().strip()) ** 2 + float(self.view.height_entry.get().strip()) ** 2)
        umbermoot = 2 * float(self.view.radius_entry.get().strip()) + 2 * float(self.view.height_entry.get().strip())
        pindala = float(self.view.radius_entry.get().strip()) * float(self.view.height_entry.get().strip())
        self.view.text_box.config(state="normal")
        self.view.text_box.insert("insert", "Külg: " + str(self.model.cylinder.radius) + "\n")
        self.view.text_box.insert("insert", "Külg: " + str(self.model.cylinder.height) + "\n") # kirjuta tulemus kasti
        self.view.text_box.insert("insert", "Diagonaal: " + str(diagonaal) + "\n")
        self.view.text_box.insert("insert", "Ümbermõõt: " + str(umbermoot) + "\n")
        self.view.text_box.insert("insert", "Pindala: " + str(pindala) + "\n")
        self.view.text_box.see("end")
        self.view.text_box.config(state="disabled")
        self.view.btn_arvuta.config(state="disabled")









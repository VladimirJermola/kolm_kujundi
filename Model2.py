import sys
from tkinter import messagebox
from Rectangle import Cylinder


class Model:
    def __init__(self):
        self.__radius = 0.0
        self.__height = 0.0
        self.cylinder = Cylinder()



    #GETTERS
    @property
    def radius(self):
        return self.__radius

    @property
    def height(self):
        return self.__height

    @staticmethod
    def is_number(user_input):
        try:
            i = float(user_input)
            if i > 0:
                return True
        except ValueError:
            return False

    def get_user_input_radius(self, user_input):
        if self.is_number(user_input):
            self.cylinder.radius = float(user_input)
        else:
            if messagebox.showerror("Viga", "Külg on vigane. Külg peab olema positiivne arv."):
                sys.exit(1)


    def get_user_input_height(self, user_input):
        if self.is_number(user_input):
            self.cylinder.height = float(user_input)
        else:
            if messagebox.showerror("Viga", "Külg on vigane. Külg peab olema positiivne arv."):
                sys.exit(1)




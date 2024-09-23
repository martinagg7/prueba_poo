from superclases.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, tipo, ruedas=2):
        super().__init__(color, ruedas)  
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta {self.marca} ({self.modelo}, {self.color}, {self.ruedas} ruedas)"
    

    def arrancar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está lista para rodar.")

    def frenar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está frenando.")

   
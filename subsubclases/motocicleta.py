from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, color, modelo, num_ruedas, cilindrada, tipo):
        super().__init__(marca, modelo, color, tipo, num_ruedas)  
        self.cilindrada = cilindrada  

    def __str__(self):
        return f"Motocicleta {self.marca} ({self.modelo}, {self.color}, {self.cilindrada} cc)"        
    def arrancar(self):
        print("Arrancando la motocicleta")

    def pedalear(self):
        print("Las motocicletas no se pedalean")

    
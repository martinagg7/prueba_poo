from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, color, modelo, num_ruedas, cilindrada, tipo):
        super().__init__(marca, modelo, color, tipo, num_ruedas)  # Llamada correcta a Bicicleta
        self.cilindrada = cilindrada  # Atributo específico de Motocicleta
    def arrancar(self):
        print("Arrancando la motocicleta")

    def pedalear(self):
        print("Las motocicletas no se pedalean")

    def __str__(self):
        return f"Motocicleta(marca={self.marca}, modelo={self.modelo}, color={self.color}, tipo={self.tipo}, cilindrada={self.cilindrada})"
    

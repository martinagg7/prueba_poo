from subclases.coche import Coche

class Camioneta(Coche):
    def __init__(self, marca, modelo, color, ruedas, capacidad_carga, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.marca = marca
        self.modelo = modelo
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"Camioneta {self.marca} ({self.modelo}, {self.color}, {self.capacidad_carga} kg, {self.cilindrada} cc)"
      
    

    
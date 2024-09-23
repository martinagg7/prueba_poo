from superclases.vehiculo import Vehiculo

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
    		return f"Coche ({self.color}, {self.velocidad} km/h, {self.ruedas} ruedas, {self.cilindrada} cc)"

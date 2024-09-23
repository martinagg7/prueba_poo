from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta


def lanzador_main():
    vehiculos = []

    # Creación de vehículos
    mi_vehiculo = Coche("Rojo", 4, 180, 2000)
    vehiculos.append(mi_vehiculo)

    mi_vehiculo2 = Bicicleta("Azul", "Montaña", "Azul", "Deportiva", 2)
    vehiculos.append(mi_vehiculo2)

    mi_vehiculo3 = Camioneta("Ford", "Fiesta", "Blanco", 4, 1000, 160, 2500)
    vehiculos.append(mi_vehiculo3)

    mi_vehiculo4 = Bicicleta("Rojo", "Carretera", "Rojo", "Competición", 2)
    vehiculos.append(mi_vehiculo4)

    mi_vehiculo5 = Camioneta("Chevrolet", "Silverado", "Negro", 4, 1500, 140, 3000)
    vehiculos.append(mi_vehiculo5)

    mi_vehiculo6 = Motocicleta("Honda", "Touring", "Blanca", 2, 1200, "Touring")
    vehiculos.append(mi_vehiculo6)

    mi_vehiculo7 = Motocicleta("Yamaha", "Deportiva", "Negra", 2, 1000, "Deportiva")
    vehiculos.append(mi_vehiculo7)

    # Función modificada para catalogar
    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
            for v in vehiculos_filtrados:
                print(v)
        else:
            print("Mostrando todos los vehículos:")
            for v in vehiculos:
                print(v)




    catalogar(vehiculos, 2)  # Vehículos con 2 ruedas
    catalogar(vehiculos, 4)  # Vehículos con 4 ruedas
    catalogar(vehiculos)     # Mostrar todos los vehículos


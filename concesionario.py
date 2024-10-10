
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Número de Puertas: {self.numero_puertas}, Automático: {'Sí' if self.es_automatico else 'No'}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Cilindraje: {self.cilindraje}cc, Tipo: {self.tipo}"


def main():
    # Crear una lista de vehículos
    vehiculos = [
        Auto("Toyota", "Corolla", 2020, 4, True),
        Auto("Ford", "Fiesta", 2019, 4, False),
        Moto("Honda", "CBR500R", 2021, 500, "Deportiva"),
        Moto("Yamaha", "NMAX", 2022, 155, "Scooter"),
    ]

    # Mostrar la información de cada vehículo
    for vehiculo in vehiculos:
        print(vehiculo.mostrar_info())


if __name__ == "__main__":
    main()

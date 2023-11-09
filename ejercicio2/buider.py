from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass 


    @abstractmethod
    def masa(self):
        pass

    @abstractmethod
    def salsa_base(self):
        pass

    @abstractmethod
    def ingredientes(self):
        pass

    @abstractmethod
    def coccion(self):
        pass

    @abstractmethod
    def presentacion(self):
        pass

    @abstractmethod
    def maridaje(self):
        pass

    @abstractmethod
    def extra(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Builder()

    @property
    def pizza(self) -> Builder:
        pizza = self._pizza
        self.reset()  # Restablece el builder para construir una nueva pizza
        return pizza

    def tipo_masa(self) -> None:
        masa = input("¿Qué tipo de masa quieres? (Por ejemplo: fina, normal, gruesa): ")
        self._pizza.add("Tipo de Masa", masa)

    def salsa_base(self) -> None:
        salsa = input("¿Qué salsa quieres? (Por ejemplo: tomate, barbacoa, carbonara): ")
        self._pizza.add("Salsa Base", salsa)

    def ingr_principales(self) -> None:
        ingredientes = []
        while True:
            ingrediente = input("¿Qué ingrediente quieres? (Si no quieres ninguno, pulsa Enter para salir): ")
            if not ingrediente:
                break
            ingredientes.append(ingrediente)
        self._pizza.add("Ingredientes Principales", ingredientes)

    def tec_coccion(self) -> None:
        coccion = input("¿Qué técnica de cocción quieres? (Por ejemplo: horno de leña, horno eléctrico, horno de gas): ")
        self._pizza.add("Técnica de Cocción", coccion)

    def presentacion(self) -> None:
        presentacion = input("¿Cómo quieres que se presente? (Por ejemplo: en caja de cartón, en plato de barro): ")
        self._pizza.add("Presentación", presentacion)

    def maridajes(self) -> None:
        maridajes = []
        while True:
            maridaje = input("¿Qué maridaje quieres? (Si no quieres ninguno, pulsa Enter para salir): ")
            if not maridaje:
                break
            maridajes.append(maridaje)
        self._pizza.add("Maridajes", maridajes)

    def extras(self) -> None:
        extras = []
        while True:
            extra = input("¿Qué extra quieres? (Por ejemplo: bordes especiales, ingrediente extra, etc.)(Si no quieres ninguno, pulsa Enter para salir): ")
            if not extra:
                break
            extras.append(extra)
        self._pizza.add("Extras", extras)


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_pizza(self) -> None:
        self.builder.masa()
        self.builder.salsa_base()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridaje()
        self.builder.extra()


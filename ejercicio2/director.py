from ejercicio2 import Builder

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

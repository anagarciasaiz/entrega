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
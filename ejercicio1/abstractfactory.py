from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

class AbstractFactory(ABC):

    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def moda(self) -> AbstractModa:
        pass

    @abstractmethod
    def media(self) -> AbstractMedia:
        pass

    

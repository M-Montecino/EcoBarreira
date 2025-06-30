from daos.dao import DAO
from model.ecobarreira import EcoBarreira
from model.sensor import Sensor


class EcobarreiraDAO(DAO):
    def __init__(self):
        super().__init__('ecobarreiras.pkl')

    def adiciona(self, ecobarreira: EcoBarreira):
        if ecobarreira is not None and \
                isinstance(ecobarreira, EcoBarreira) and \
                isinstance(ecobarreira.codigo, int):
            super().adiciona(ecobarreira)

    def altera(self, ecobarreira: EcoBarreira):
        if ecobarreira is not None and \
                isinstance(ecobarreira, EcoBarreira) and \
                isinstance(ecobarreira.codigo, int):
            super().altera(ecobarreira)

    def pega(self, codigo: int):
        if isinstance(codigo, int):
            return super().pega(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            super().remove(codigo)

    def pega_todos(self):
        return super().pega_todos()
    
    def adiciona_sensor(self, ecobarreira: EcoBarreira, sensor: Sensor):
        return ecobarreira.adicionar_sensor(sensor)
    
    def remover_sensor(self, ecobarreira: EcoBarreira, sensor:Sensor):
        return ecobarreira.remover_sensor(sensor)
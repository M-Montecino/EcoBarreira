from daos.dao import DAO
from model.sensor import Sensor


class SensorDAO(DAO):
    def __init__(self):
        super().__init__('sensores.pkl', chave="codigo")

    def adiciona(self, sensor: Sensor):
        if sensor is not None and \
                isinstance(sensor, Sensor) and \
                isinstance(sensor.codigo, int):
            super().adiciona(sensor)

    def altera(self, sensor: Sensor):
        if sensor is not None and \
                isinstance(sensor, Sensor) and \
                isinstance(sensor.codigo, int):
            super().altera(sensor)

    def pega(self, codigo: int):
        if isinstance(codigo, int):
            return super().pega(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            super().remove(codigo)

    def pega_todos(self):
        return super().pega_todos()
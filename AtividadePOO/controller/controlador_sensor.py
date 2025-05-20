from model.sensor import Sensor
from view.tela_sensor import TelaSensor


class ControladorSensor():
    def __init__(self, controlador_sistema):
        self.__sensores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_sensor = TelaSensor()

    def cadastrar_sensor(self):
        dados_sensor = self.__tela_sensor.pega_dados_sensor()
        novo_sensor = Sensor(dados_sensor["codigo"],
                        dados_sensor["tipo"],
                        dados_sensor["ativo"]
                        )
        for sensor in self.__sensores:
            if sensor.codigo == novo_sensor.codigo:
                self.__tela_sensor.mostra_mensagem("Atenção! Esse sensor já existe")
                return
        self.__sensores.append(novo_sensor)
        self.__tela_sensor.mostra_mensagem("Sensor criado com sucesso!")
        return

    def buscar_sensor_por_codigo(self, codigo:int):
        for sensor in self.__sensores:
            if sensor.codigo == codigo:
                return sensor
        return None

    def altera_sensor(self):
        self.listar_sensores()
        codigo_sensor = self.__tela_sensor.busca_sensor()
        sensor = self.buscar_sensor_por_codigo(codigo_sensor)

        if sensor is not None:
            novos_dados_sensor = self.__tela_sensor.pega_dados_sensor()
            sensor.codigo = novos_dados_sensor["codigo"]
            sensor.tipo = novos_dados_sensor["tipo"]
            sensor.ativo = novos_dados_sensor["ativo"]
            self.listar_sensores()
            self.__tela_sensor.mostra_mensagem("Sensor alterado com sucesso!")
        else:
            self.__tela_sensor.mostra_mensagem("Atenção! Esse sensor não existe")


    def excluir_sensor(self, codigo:int):
        self.listar_sensores()
        codigo = self.__tela_sensor.busca_sensor()
        sensor = self.buscar_sensor_por_codigo(codigo)

        if sensor is not None:
            self.__sensores.remove(sensor)
            self.listar_sensores()
            self.__tela_sensor.mostra_mensagem("Sensor excluido com sucesso!")
        else:
            self.__tela_sensor.mostra_mensagem("Atenção! Esse sensor não existe")
    
    def listar_sensores(self):
        for sensor in self.__sensores:
            self.__tela_sensor.mostra_sensor({"Código": sensor.codigo,
                                              "Tipo": sensor.tipo,
                                              "Ativo": sensor.ativo})
    
    def retomar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_sensor, 2: self.buscar_sensor_por_codigo,
                        3: self.altera_sensor, 4: self.excluir_sensor,
                        5: self.listar_sensores}

        continua = True
        while continua:
            lista_opcoes[self.__tela_sensor.tela_opcoes()]()

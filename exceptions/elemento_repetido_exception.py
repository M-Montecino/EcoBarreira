class ElementoRepetidoException(Exception):
    def __init__(self):
        super().__init__("Atenção! Esse elemento já existe")
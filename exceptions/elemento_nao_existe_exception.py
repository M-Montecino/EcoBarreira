class ElementoNaoExisteException(Exception):
    def __init__(self):
        super().__init__("Atenção! Esse elemento não existe")
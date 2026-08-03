from helpers.logger import logger
from repository.GalinaceosRepository import GalinaceosRepository

class GalinaceosService():
    def __init__(self):
        self.repo = GalinaceosRepository()

    def getAll(self, filtros: dict = None):
        registros = self.repo.getAll(filtros)
        logger.info(f"Retornando {len(registros)} galináceos")
        return registros
from helpers.logger import logger
from repository.AvicolaRepository import AvicolaRepository

class AvicolaService():
    def __init__(self):
        self.avicolaRepository = AvicolaRepository()

    def getAll(self, filtros: dict = None):
        avicolas = self.avicolaRepository.getAll(filtros)
        logger.info(f"Retornando {len(avicolas)} avícolas")
        return avicolas

    def getByIdAvicola(self, id):
        avicola = self.avicolaRepository.getByIdAvicola(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return avicola

    def create(self, data):
        avicola = self.avicolaRepository.insert(
            data["nome"], data["tipo"], data["capacidade"]
        )
        logger.info(f"Avícola criada com id: {avicola.id}")
        return avicola

    def update(self, id, data):
        avicola = self.avicolaRepository.update(
            id, data["nome"], data["tipo"], data["capacidade"]
        )
        if avicola is None:
            return None
        logger.info(f"Avícola {id} atualizada")
        return avicola

    def delete(self, id):
        removido = self.avicolaRepository.delete(id)
        logger.info(f"Avícola {id} removida: {removido}")
        return removido

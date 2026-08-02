from helpers.logger import logger
from repository.AvicultorRepository import AvicultorRepository


class AvilcultorService():
    def __init__(self):
        self.avicultorRepository = AvicultorRepository()

    def getAll(self, filtros: dict = None):
        avicultores = self.avicultorRepository.getAll(filtros)
        logger.info(f"Retornando {len(avicultores)} avicultores")
        return avicultores

    def getByIdAvicultor(self, id):
        avicultor = self.avicultorRepository.getByIdAvicultor(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return avicultor

    def create(self, data):
        avicultor = self.avicultorRepository.insert(
            data["nome"], data["nascimento"], data["cpf"], data["caf"]
        )
        logger.info(f"Avicultor criado com id: {avicultor.id}")
        return avicultor

    def update(self, id, data):
        avicultor = self.avicultorRepository.update(
            id, data["nome"], data["nascimento"], data["cpf"], data["caf"]
        )
        if avicultor is None:
            return None
        logger.info(f"Avicultor {id} atualizado")
        return avicultor

    def delete(self, id):
        removido = self.avicultorRepository.delete(id)
        logger.info(f"Avicultor {id} removido: {removido}")
        return removido
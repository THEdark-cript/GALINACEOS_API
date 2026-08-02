from helpers.logger import logger
from repository.AviarioRepository import AviarioRepository

class AviarioService():
    def __init__(self):
        self.aviarioRepository = AviarioRepository()

    def getAll(self, filtros: dict = None):
        aviarios = self.aviarioRepository.getAll(filtros)
        logger.info(f"Retornando {len(aviarios)} aviários")
        return aviarios

    def getByIdAviario(self, id):
        aviario = self.aviarioRepository.getByIdAviario(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return aviario

    def create(self, data):
        aviario = self.aviarioRepository.insert(
            data["nome"], data["localizacao"], data["capacidade"]
        )
        logger.info(f"Aviário criado com id: {aviario.id}")
        return aviario

    def update(self, id, data):
        aviario = self.aviarioRepository.update(
            id, data["nome"], data["localizacao"], data["capacidade"]
        )
        if aviario is None:
            return None
        logger.info(f"Aviário {id} atualizado")
        return aviario

    def delete(self, id):
        removido = self.aviarioRepository.delete(id)
        logger.info(f"Aviário {id} removido: {removido}")
        return removido

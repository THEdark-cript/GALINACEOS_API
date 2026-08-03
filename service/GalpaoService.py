from helpers.logger import logger
from repository.GalpaoRepository import GalpaoRepository

class GalpaoService():
    def __init__(self):
        self.galpaoRepository = GalpaoRepository()

    def getAll(self, filtros: dict = None):
        galpoes = self.galpaoRepository.getAll(filtros)
        logger.info(f"Retornando {len(galpoes)} galpões")
        return galpoes

    def getByIdGalpao(self, id):
        galpao = self.galpaoRepository.getByIdGalpao(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return galpao

    def create(self, data):
        galpao = self.galpaoRepository.insert(
            data["nome"], data["capacidade"], data["avicola_id"]
        )
        logger.info(f"Galpão criado com id: {galpao.id}")
        return galpao
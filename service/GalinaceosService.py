from helpers.logger import logger
from repository.GalinaceosRepository import GalinaceosRepository

class GalinaceosService():
    def __init__(self):
        self.repo = GalinaceosRepository()

    def getAll(self, filtros: dict = None):
        registros = self.repo.getAll(filtros)
        logger.info(f"Retornando {len(registros)} galináceos")
        return registros

    def getById(self, id):
        registo = self.repo.getById(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return registo

    def create(self, data):
        galinaceo = self.repo.insert(
            data["sist_cria"], data["niv_terr"], data.get("cod_terr"),
            data["nom_terr"], data["cl_gal"], data["nom_cl_gal"], data.get("gal_total")
        )
        logger.info(f"Galináceo criado com id: {galinaceo.id}")
        return galinaceo

    def update(self, id, data):
        galinaceo = self.repo.update(
            id, data["sist_cria"], data["niv_terr"], data.get("cod_terr"),
            data["nom_terr"], data["cl_gal"], data["nom_cl_gal"], data.get("gal_total")
        )
        if galinaceo is None:
            return None
        logger.info(f"Galináceo {id} atualizado")
        return galinaceo

    def delete(self, id):
        removido = self.repo.delete(id)
        logger.info(f"Galináceo {id} removido: {removido}")
        return removido

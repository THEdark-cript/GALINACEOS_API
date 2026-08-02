from marshmallow import ValidationError

from helpers.logger import logger
from repository.EnderecoRepository import EnderecoRepository
from service.AvicultoresService import AvilcultorService


class EnderecoService():
    def __init__(self):
        self.enderecoRepository = EnderecoRepository()

    def _validarAvicultor(self, avicultor_id):
        avicultor = AvilcultorService().getByIdAvicultor(avicultor_id)
        if avicultor is None:
            raise ValidationError({"avicultor_id": ["Avicultor não encontrado."]})

    def getAll(self, filtros: dict = None):
        enderecos = self.enderecoRepository.getAll(filtros)
        logger.info(f"Retornando {len(enderecos)} endereços")
        return enderecos

    def getByIdEndereco(self, id):
        endereco = self.enderecoRepository.getByIdEndereco(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return endereco

    def create(self, data):
        self._validarAvicultor(data["avicultor_id"])
        endereco = self.enderecoRepository.insert(
            data.get("logradouro"), data["cep"], data.get("numero"), data["avicultor_id"]
        )
        logger.info(f"Endereço criado com id: {endereco.id}")
        return endereco

    def update(self, id, data):
        self._validarAvicultor(data["avicultor_id"])
        endereco = self.enderecoRepository.update(
            id, data.get("logradouro"), data["cep"], data.get("numero"), data["avicultor_id"]
        )
        if endereco is None:
            return None
        logger.info(f"Endereço {id} atualizado")
        return endereco

    def delete(self, id):
        removido = self.enderecoRepository.delete(id)
        logger.info(f"Endereço {id} removido: {removido}")
        return removido
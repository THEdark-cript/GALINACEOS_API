from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from models.Endereco import EnderecoSchema, endereco_fields
from service.EnderecoService import EnderecoService
from helpers.logger import logger

CAMPOS_FILTRO = {"avicultor_id", "cep"}


class EnderecosController(Resource):
    def get(self):
        logger.info("Listando todos os endereços")
        filtros = {k: v for k, v in request.args.items()
                   if k in CAMPOS_FILTRO and v}
        enderecos = EnderecoService().getAll(filtros)
        return marshal(enderecos, endereco_fields), 200

    def post(self):
        try:
            data = EnderecoSchema().load(request.get_json())
            endereco = EnderecoService().create(data)
            return marshal(endereco, endereco_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400


class EnderecoController(Resource):
    def get(self, endereco_id):
        logger.info(f"Listando endereço pelo id: {endereco_id}")
        endereco = EnderecoService().getByIdEndereco(endereco_id)
        if endereco is None:
            return {"mensagem": "O endereço não foi encontrado"}, 404
        return marshal(endereco, endereco_fields), 200

    def put(self, endereco_id):
        try:
            data = EnderecoSchema().load(request.get_json())
            endereco = EnderecoService().update(endereco_id, data)
            if endereco is None:
                return {"mensagem": "O endereço não foi encontrado"}, 404
            return marshal(endereco, endereco_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, endereco_id):
        logger.info(f"Removendo endereço id: {endereco_id}")
        removido = EnderecoService().delete(endereco_id)
        if not removido:
            return {"mensagem": "O endereço não foi encontrado"}, 404
        return {"mensagem": "Endereço removido com sucesso!"}, 200
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

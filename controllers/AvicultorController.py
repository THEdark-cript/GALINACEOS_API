from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from models.Avicultor import AvicultorSchema, avicultor_fields, avicultor_id_fields
from service.AvicultoresService import AvilcultorService
from helpers.logger import logger

CAMPOS_FILTRO = {"nome", "cpf", "caf"}


class AvicultoresController(Resource):
    def get(self):
        logger.info("Listando todos os avicultores")
        filtros = {k: v for k, v in request.args.items()
                   if k in CAMPOS_FILTRO and v}
        avicultores = AvilcultorService().getAll(filtros)
        return marshal(avicultores, avicultor_fields), 200

    def post(self):
        try:
            data = AvicultorSchema().load(request.get_json())
            avicultor = AvilcultorService().create(data)
            return marshal(avicultor, avicultor_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400


class AvicultorController(Resource):
    def get(self, avicultor_id):
        logger.info(f"Listando avicultor pelo id: {avicultor_id}")
        avicultor = AvilcultorService().getByIdAvicultor(avicultor_id)
        if avicultor is None:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return marshal(avicultor, avicultor_fields), 200

    def put(self, avicultor_id):
        try:
            data = AvicultorSchema().load(request.get_json())
            avicultor = AvilcultorService().update(avicultor_id, data)
            if avicultor is None:
                return {"mensagem": "O avicultor não foi encontrado"}, 404
            return marshal(avicultor, avicultor_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, avicultor_id):
        logger.info(f"Removendo avicultor id: {avicultor_id}")
        removido = AvilcultorService().delete(avicultor_id)
        if not removido:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return {"mensagem": "Avicultor removido com sucesso!"}, 200
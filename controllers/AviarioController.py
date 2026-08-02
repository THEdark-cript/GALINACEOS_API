from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError
from models.Aviario import AviarioSchema, aviario_fields
from service.AviarioService import AviarioService
from helpers.logger import logger

CAMPOS_FILTRO = {"nome", "localizacao"}

class AviariosController(Resource):
    def get(self):
        logger.info("Listando todos os aviários")
        filtros = {k: v for k, v in request.args.items()
                   if k in CAMPOS_FILTRO and v}
        aviarios = AviarioService().getAll(filtros)
        return marshal(aviarios, aviario_fields), 200

    def post(self):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().create(data)
            return marshal(aviario, aviario_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400


class AviarioController(Resource):
    def get(self, aviario_id):
        logger.info(f"Buscando aviário pelo id: {aviario_id}")
        aviario = AviarioService().getByIdAviario(aviario_id)
        if aviario is None:
            return {"mensagem": "Aviário não encontrado"}, 404
        return marshal(aviario, aviario_fields), 200

    def put(self, aviario_id):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().update(aviario_id, data)
            if aviario is None:
                return {"mensagem": "Aviário não encontrado"}, 404
            return marshal(aviario, aviario_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, aviario_id):
        logger.info(f"Removendo aviário id: {aviario_id}")
        removido = AviarioService().delete(aviario_id)
        if not removido:
            return {"mensagem": "Aviário não encontrado"}, 404
        return {"mensagem": "Aviário removido com sucesso!"}, 200

from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError
from models.Galpao import GalpaoSchema, galpao_fields
from service.GalpaoService import GalpaoService
from helpers.logger import logger

CAMPOS_FILTRO = {"nome", "avicola_id"}

class GalpoesController(Resource):
    def get(self):
        logger.info("Listando todos os galpões")
        filtros = {k: v for k, v in request.args.items()
                   if k in CAMPOS_FILTRO and v}
        galpoes = GalpaoService().getAll(filtros)
        return marshal(galpoes, galpao_fields), 200

    def post(self):
        try:
            data = GalpaoSchema().load(request.get_json())
            galpao = GalpaoService().create(data)
            return marshal(galpao, galpao_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400


class GalpaoController(Resource):
    def get(self, galpao_id):
        logger.info(f"Buscando galpão pelo id: {galpao_id}")
        galpao = GalpaoService().getByIdGalpao(galpao_id)
        if galpao is None:
            return {"mensagem": "Galpão não encontrado"}, 404
        return marshal(galpao, galpao_fields), 200

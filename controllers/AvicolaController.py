from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError
from models.Avicola import AvicolaSchema, avicola_fields
from service.AvicolaService import AvicolaService
from helpers.logger import logger

CAMPOS_FILTRO = {"nome", "tipo"}

class AvicolasController(Resource):
    def get(self):
        logger.info("Listando todas as avícolas")
        filtros = {k: v for k, v in request.args.items()
                   if k in CAMPOS_FILTRO and v}
        avicolas = AvicolaService().getAll(filtros)
        return marshal(avicolas, avicola_fields), 200

    def post(self):
        try:
            data = AvicolaSchema().load(request.get_json())
            avicola = AvicolaService().create(data)
            return marshal(avicola, avicola_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400


class AvicolaController(Resource):
    def get(self, avicola_id):
        logger.info(f"Buscando avícola pelo id: {avicola_id}")
        avicola = AvicolaService().getByIdAvicola(avicola_id)
        if avicola is None:
            return {"mensagem": "Avícola não encontrada"}, 404
        return marshal(avicola, avicola_fields), 200

    def put(self, avicola_id):
        try:
            data = AvicolaSchema().load(request.get_json())
            avicola = AvicolaService().update(avicola_id, data)
            if avicola is None:
                return {"mensagem": "Avícola não encontrada"}, 404
            return marshal(avicola, avicola_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, avicola_id):
        logger.info(f"Removendo avícola id: {avicola_id}")
        removido = AvicolaService().delete(avicola_id)
        if not removido:
            return {"mensagem": "Avícola não encontrada"}, 404
        return {"mensagem": "Avícola removida com sucesso!"}, 200

from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError
from models.Galinaceos import GalinaceoSchema, galinaceo_fields
from service.GalinaceosService import GalinaceosService
from helpers.logger import logger

CAMPOS_FILTRO = {"sist_cria", "niv_terr", "cod_terr", "nom_terr", "cl_gal"}

class GalinaceosController(Resource):
    def get(self):
        logger.info("Listando todos os galináceos")
        filtros = {k: v for k, v in request.args.items()
                   if k in CAMPOS_FILTRO and v}
        registros = GalinaceosService().getAll(filtros)
        return marshal(registros, galinaceo_fields), 200

    def post(self):
        try:
            data = GalinaceoSchema().load(request.get_json())
            galinaceo = GalinaceosService().create(data)
            return marshal(galinaceo, galinaceo_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400


class GalinaceoController(Resource):
    def get(self, galinaceo_id):
        logger.info(f"Buscando galináceo pelo id: {galinaceo_id}")
        registo = GalinaceosService().getById(galinaceo_id)
        if registo is None:
            return {"mensagem": "O registro não foi encontrado"}, 404
        return marshal(registo, galinaceo_fields), 200

    def put(self, galinaceo_id):
        try:
            data = GalinaceoSchema().load(request.get_json())
            registo = GalinaceosService().update(galinaceo_id, data)
            if registo is None:
                return {"mensagem": "O registro não foi encontrado"}, 404
            return marshal(registo, galinaceo_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, galinaceo_id):
        logger.info(f"Removendo galináceo id: {galinaceo_id}")
        removido = GalinaceosService().delete(galinaceo_id)
        if not removido:
            return {"mensagem": "O registro não foi encontrado"}, 404
from flask import request
from flask_restful import Resource, marshal
from models.Galinaceos import galinaceo_fields
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
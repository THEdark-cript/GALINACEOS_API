from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.Cl_Gal import Cl_GalSchema
from service.Cl_GalService import Cl_GalService

cl_gal_bp = Blueprint('cl_gal', __name__, url_prefix='/cl_gal')

@cl_gal_bp.get("/<int:id>")
def getByIdCl_Gal(id: int):
    cl_gal = Cl_GalService().getById(id)
    if cl_gal is None:
        return {"message": "A CLASSE DE GALINÁCEOS NÃO FOI ENCONTRADA."}, 404
    return cl_gal.toDict()

@cl_gal_bp.get("/")
def getCl_Gal():
    cl_gal = Cl_GalService().getAll()
    return [cg.toDict() for cg in cl_gal], 200

@cl_gal_bp.post("/")
def postCl_Gal():
    try:
        data = Cl_GalSchema().load(request.get_json())
        cl_gal = Cl_GalService().create(data)
        return cl_gal.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@cl_gal_bp.put("/<int:id>")
def putCl_Gal(id: int):
    try:
        data = Cl_GalSchema().load(request.get_json())
        cl_gal = Cl_GalService().update(id, data)
        if cl_gal is None:
            return {"message": "A CLASSE DE GALINÁCEOS NÃO FOI ENCONTRADA."}, 404
        return cl_gal.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@cl_gal_bp.delete("/<int:id>")
def deleteCl_Gal(id: int):
    removido = Cl_GalService().delete(id)
    if not removido:
        return {"message": "A CLASSE DE GALINÁCEOS NÃO FOI ENCONTRADA."}, 404
    return {"message": "A CLASSE DE GALINÁCEOS FOI REMOVIDA COM SUCESSO."}, 200

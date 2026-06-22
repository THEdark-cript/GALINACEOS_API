from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.Cod_Terr import Cod_TerrSchema
from service.Cod_TerrService import Cod_TerrService

cod_terr_bp = Blueprint('cod_terr', __name__, url_prefix='/cod_terr')

@cod_terr_bp.get("/<int:id>")
def getByIdCod_Terr(id: int):
    cod_terr = Cod_TerrService().getById(id)
    if cod_terr is None:
        return {"message": "O CÓDIGO TERRITORIAL NÃO FOI ENCONTRADO."}, 404
    return cod_terr.toDict()

@cod_terr_bp.get("/")
def getCod_Terr():
    cod_terr = Cod_TerrService().getAll()
    return [ct.toDict() for ct in cod_terr], 200

@cod_terr_bp.post("/")
def postCod_Terr():
    try:
        data = Cod_TerrSchema().load(request.get_json())
        cod_terr = Cod_TerrService().create(data)
        return cod_terr.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@cod_terr_bp.put("/<int:id>")
def putCod_Terr(id: int):
    try:
        data = Cod_TerrSchema().load(request.get_json())
        cod_terr = Cod_TerrService().update(id, data)
        if cod_terr is None:
            return {"message": "O CÓDIGO TERRITORIAL NÃO FOI ENCONTRADO."}, 404
        return cod_terr.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@cod_terr_bp.delete("/<int:id>")
def deleteCod_Terr(id: int):
    removido = Cod_TerrService().delete(id)
    if not removido:
        return {"message": "O CÓDIGO TERRITORIAL NÃO FOI ENCONTRADO."}, 404
    return {"message": "O CÓDIGO TERRITORIAL FOI REMOVIDO COM SUCESSO."}, 200

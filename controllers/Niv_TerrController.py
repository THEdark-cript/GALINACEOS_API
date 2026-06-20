from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.Niv_Terr import Niv_TerrSchema
from services.Niv_TerrService import Niv_TerrService

niv_terr_bp = Blueprint('niv_terr', __name__, url_prefix='/niv_terr')

@niv_terr_bp.get("/<int:id>")
def getByIdNiv_Terr(id: int):
    niv_terr = Niv_TerrService().getById(id)
    if niv_terr is None:
        return {"message": "O NÍVEL TERRITORIAL NÃO FOI ENCONTRADO."}, 404
    return niv_terr.toDict()

@niv_terr_bp.get("/")
def getNiv_Terr():
    niv_terr = Niv_TerrService().getALL()
    return [nt.toDict() for nt in niv_terr], 200

@niv_terr_bp.post("/")
def postNiv_Terr():
    try:
        data = Niv_TerrSchema().load(request.get_json())
        niv_terr = Niv_TerrService().create(data)
        return niv_terr.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@niv_terr_bp.put("/<int:id>")
def putNiv_Terr(id: int):
    try:
        data = Niv_TerrSchema().load(request.get_json())
        niv_terr = Niv_TerrService().update(id, data)
        if niv_terr is None:
            return {"message": "O NÍVEL TERRITORIAL NÃO FOI ENCONTRADO."}, 404
        return niv_terr.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@niv_terr_bp.delete("/<int:id>")
def deleteNiv_Terr(id: int):
    removido = Niv_TerrService().delete(id)
    if not removido:
        return {"message": "O NÍVEL TERRITORIAL NÃO FOI ENCONTRADO."}, 404
    return {"message": "O NÍVEL TERRITORIAL FOI REMOVIDO COM SUCESSO."}, 200

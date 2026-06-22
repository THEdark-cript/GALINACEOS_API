from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.Nom_Terr import Nom_TerrSchema
from service.Nom_TerrService import Nom_TerrService

nom_terr_bp = Blueprint('nom_terr', __name__, url_prefix='/nom_terr')

@nom_terr_bp.get("/<int:id>")
def getByIdNom_Terr(id: int):
    nom_terr = Nom_TerrService().getById(id)
    if nom_terr is None:
        return {"message": "O NOME TERRITORIAL NÃO FOI ENCONTRADO."}, 404
    return nom_terr.toDict()

@nom_terr_bp.get("/")
def getNom_Terr():
    nom_terr = Nom_TerrService().getAll()
    return [nt.toDict() for nt in nom_terr], 200

@nom_terr_bp.post("/")
def postNom_Terr():
    try:
        data = Nom_TerrSchema().load(request.get_json())
        nom_terr = Nom_TerrService().create(data)
        return nom_terr.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@nom_terr_bp.put("/<int:id>")
def putNom_Terr(id: int):
    try:
        data = Nom_TerrSchema().load(request.get_json())
        nom_terr = Nom_TerrService().update(id, data)
        if nom_terr is None:
            return {"message": "O NOME TERRITORIAL NÃO FOI ENCONTRADO."}, 404
        return nom_terr.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@nom_terr_bp.delete("/<int:id>")
def deleteNom_Terr(id: int):
    removido = Nom_TerrService().delete(id)
    if not removido:
        return {"message": "O NOME TERRITORIAL NÃO FOI ENCONTRADO."}, 404
    return {"message": "O NOME TERRITORIAL FOI REMOVIDO COM SUCESSO."}, 200

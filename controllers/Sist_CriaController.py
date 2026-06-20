from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.Sist_Cria import Sist_CriaSchema
from services.Sist_CriaService import Sist_CriaService

sist_cria_bp = Blueprint('sist_cria',__name__, url_prefix='/sist_cria')


@sist_cria_bp.get("/<int:id>")

def getByIdSist_Cria(id: int):
    sist_cria = Sist_CriaService().getById(id)
    if sist_cria is None:
        return {"message": "O SISTEMA DE CRIAÇÃO NÃO FOI ENCONTRADO."},404
    return sist_cria.toDict()



@sist_cria_bp.get("/")
def getsist_criacoes():
    sist_cria= Sist_CriaService().getALL()
    return [sc.toDict() for sc in sist_cria],200



@sist_cria_bp.post("/")
def postSist_Cria():
    try:
        data = Sist_CriaSchema().load(request.get_json())
        sist_cria = Sist_CriaService().create(data)
        return sist_cria.toDict(),201
    except ValidationError as err:
       return jsonify(err.messages),400
    

@sist_cria_bp.put("/<int:id>")
def putsist_criacoes(id: int):
    try:
        data = Sist_CriaSchema().load(request.get_json())
        sist_cria = Sist_CriaService().update(id, data)
        if sist_cria is None:
            return {"message": "O SISTEMA DE CRIAÇÃO NÃO FOI ENCONTRADO."},404
        return sist_cria.toDict(),200
    except ValidationError as err:
        return jsonify(err.messages),400
    

@sist_cria_bp.delete("/<int:id>")
def deleteSist_Cria(id: int):
    removido = Sist_CriaService().delete(id)
    if not removido:
        return {"message": "O SISTEMA DE CRIAÇÃO NÃO FOI ENCONTRADO."},404
    return {"message": "O SISTEMA DE CRIAÇÃO FOI REMOVIDO COM SUCESSO."},200
        

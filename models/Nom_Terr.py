from marshmallow import Schema, fields

class Nom_Terr:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao
        }

class Nom_TerrSchema(Schema):
    nome = fields.Str(required=True)
    descricao = fields.Str(required=True)

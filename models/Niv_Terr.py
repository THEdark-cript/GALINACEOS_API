from marshmallow import Schema, fields

class Niv_Terr:
    def __init__(self, id, nivel, descricao):
        self.id = id
        self.nivel = nivel
        self.descricao = descricao

    def toDict(self):
        return {
            "id": self.id,
            "nivel": self.nivel,
            "descricao": self.descricao
        }

class Niv_TerrSchema(Schema):
    nivel = fields.Str(required=True)
    descricao = fields.Str(required=True)

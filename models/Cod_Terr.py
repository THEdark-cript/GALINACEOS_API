from marshmallow import Schema, fields

class Cod_Terr:
    def __init__(self, id, codigo, descricao):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao

    def toDict(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "descricao": self.descricao
        }

class Cod_TerrSchema(Schema):
    codigo = fields.Str(required=True)
    descricao = fields.Str(required=True)

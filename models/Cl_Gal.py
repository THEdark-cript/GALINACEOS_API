from marshmallow import Schema, fields

class Cl_Gal:
    def __init__(self, id, sigla, descricao):
        self.id = id
        self.sigla = sigla
        self.descricao = descricao

    def toDict(self):
        return {
            "id": self.id,
            "sigla": self.sigla,
            "descricao": self.descricao
        }

class Cl_GalSchema(Schema):
    sigla = fields.Str(required=True)
    descricao = fields.Str(required=True)

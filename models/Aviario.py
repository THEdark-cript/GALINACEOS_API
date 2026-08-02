from marshmallow import Schema, fields, validate
from flask_restful import fields as dto
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from helpers.database import db

aviario_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'localizacao': dto.String,
    'capacidade': dto.Integer,
}

aviario_id_fields = {
    'id': dto.Integer
}

class Aviario(db.Model):
    __tablename__ = "tb_aviario"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", String())
    localizacao: Mapped[str] = mapped_column("localizacao", String())
    capacidade: Mapped[int] = mapped_column("capacidade", Integer)

    def __init__(self, id, nome, localizacao, capacidade):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.capacidade = capacidade

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "localizacao": self.localizacao,
            "capacidade": self.capacidade
        }


class AviarioSchema(Schema):
    nome = fields.Str(required=True, error_messages={"required": "Adicione um nome."})
    localizacao = fields.Str(required=True, error_messages={"required": "Adicione uma localização."})
    capacidade = fields.Int(required=True, validate=validate.Range(min=1), error_messages={"required": "Adicione a capacidade."})

from marshmallow import Schema, fields, validate
from flask_restful import fields as dto
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from helpers.database import db

avicola_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'tipo': dto.String,
    'capacidade': dto.Integer,
}

avicola_id_fields = {
    'id': dto.Integer
}

class Avicola(db.Model):
    __tablename__ = "tb_avicola"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", String())
    tipo: Mapped[str] = mapped_column("tipo", String())
    capacidade: Mapped[int] = mapped_column("capacidade", Integer)

    def __init__(self, id, nome, tipo, capacidade):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.capacidade = capacidade

    def toDict(self):
        return {"id": self.id, "nome": self.nome, "tipo": self.tipo, "capacidade": self.capacidade}


class AvicolaSchema(Schema):
    nome = fields.Str(required=True, error_messages={"required": "Adicione um nome."})
    tipo = fields.Str(required=True, error_messages={"required": "Adicione um tipo."})
    capacidade = fields.Int(required=True, validate=validate.Range(min=1), error_messages={"required": "Adicione a capacidade."})

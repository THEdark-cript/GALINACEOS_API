from marshmallow import Schema, fields, validate
from flask_restful import fields as dto
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db

galpao_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'capacidade': dto.Integer,
    'avicola_id': dto.Integer,
}

galpao_id_fields = {
    'id': dto.Integer
}

class Galpao(db.Model):
    __tablename__ = "tb_galpao"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    nome: Mapped[str] = mapped_column("nome", String())
    capacidade: Mapped[int] = mapped_column("capacidade", Integer)
    avicola_id: Mapped[int] = mapped_column("avicola_id", Integer, ForeignKey("tb_avicola.id"))

    # Relacionamento com Avícola
    avicola = relationship("Avicola", backref="galpoes")

    def __init__(self, id, nome, capacidade, avicola_id):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade
        self.avicola_id = avicola_id

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "capacidade": self.capacidade,
            "avicola_id": self.avicola_id
        }


class GalpaoSchema(Schema):
    nome = fields.Str(required=True, error_messages={"required": "Adicione um nome."})
    capacidade = fields.Int(required=True, validate=validate.Range(min=1), error_messages={"required": "Adicione a capacidade."})
    avicola_id = fields.Int(required=True, error_messages={"required": "Informe o ID da avícola."})

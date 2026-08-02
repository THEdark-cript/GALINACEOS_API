from typing import List
from marshmallow import Schema, fields, validate
from flask_restful import fields as dto

from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db


avicultor_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'nascimento': dto.DateTime(dt_format='iso8601'),
    'cpf': dto.String,
    'caf': dto.String,
}

avicultor_id_fields = {
    'id': dto.Integer
}


class Avicultor(db.Model):
    __tablename__ = "tb_avicultor"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    nome: Mapped[str] = mapped_column("nome", String())
    nascimento: Mapped[datetime] = mapped_column("nascimento", DateTime)
    cpf: Mapped[str] = mapped_column("cpf", String(11))
    caf: Mapped[str] = mapped_column("caf", String())

    # Referencia entre os objetos.
    enderecos: Mapped[List["Endereco"]] = relationship(
        back_populates="avicultor", cascade="all, delete-orphan"
    )

    def __init__(self, id, nome, nascimento, cpf, caf):
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.caf = caf

    def toDict(self):
        return {"id": self.id, "nome": self.nome, "nascimento": self.nascimento, "cpf": self.cpf, "caf": self.caf}


class AvicultorSchema(Schema):
    nome = fields.Str(required=True, error_messages={
                      "required": "Adicione um nome."})
    nascimento = fields.Date(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(
        max=11, error="Tamanho do CPF inválido."), error_messages={"required": "Adicione um CPF.", "invalid": "Valor inválido."})
    caf = fields.Str(required=True)
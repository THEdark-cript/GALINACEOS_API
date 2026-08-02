from marshmallow import Schema, fields, validate
from flask_restful import fields as dto

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from helpers.database import db


endereco_fields = {
    'id': dto.Integer,
    'logradouro': dto.String,
    'cep': dto.String,
    'numero': dto.Integer,
    'avicultor_id': dto.Integer,
}

endereco_id_fields = {
    'id': dto.Integer
}


class Endereco(db.Model):

    __tablename__ = "tb_endereco"
    id: Mapped[int] = mapped_column(primary_key=True)
    logradouro: Mapped[str] = mapped_column(String(), nullable=True)
    cep: Mapped[str] = mapped_column(String(8))
    numero: Mapped[int] = mapped_column(nullable=True)

    # Referência entre as tabelas.
    avicultor_id: Mapped[int] = mapped_column(ForeignKey("tb_avicultor.id"))

    avicultor: Mapped["Avicultor"] = relationship(back_populates="enderecos")

    def __init__(self, logradouro, cep, numero, avicultor_id):
        self.logradouro = logradouro
        self.cep = cep
        self.numero = numero
        self.avicultor_id = avicultor_id


class EnderecoSchema(Schema):
    logradouro = fields.Str(required=False, allow_none=True)
    cep = fields.Str(required=True, validate=validate.Length(
        equal=8, error="CEP deve ter 8 dígitos."), error_messages={"required": "Adicione um CEP."})
    numero = fields.Int(required=False, allow_none=True)
    avicultor_id = fields.Int(required=True, error_messages={
                               "required": "Informe o avicultor."})
from marshmallow import Schema, fields
from flask_restful import fields as dto
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from helpers.database import db

galinaceo_fields = {
    'id': dto.Integer,
    'sist_cria': dto.String,
    'niv_terr': dto.String,
    'cod_terr': dto.String,
    'nom_terr': dto.String,
    'cl_gal': dto.String,
    'nom_cl_gal': dto.String,
    'gal_total': dto.Integer,
}

galinaceo_id_fields = {
    'id': dto.Integer
}

class Galinaceo(db.Model):
    __tablename__ = "galinaceos"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    sist_cria: Mapped[str] = mapped_column("sist_cria", String())
    niv_terr: Mapped[str] = mapped_column("niv_terr", String())
    cod_terr: Mapped[str] = mapped_column("cod_terr", String())
    nom_terr: Mapped[str] = mapped_column("nom_terr", String())
    cl_gal: Mapped[str] = mapped_column("cl_gal", String())
    nom_cl_gal: Mapped[str] = mapped_column("nom_cl_gal", String())
    gal_total: Mapped[int] = mapped_column("gal_total", Integer)

    def __init__(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total):
        self.id = id
        self.sist_cria = sist_cria
        self.niv_terr = niv_terr
        self.cod_terr = cod_terr
        self.nom_terr = nom_terr
        self.cl_gal = cl_gal
        self.nom_cl_gal = nom_cl_gal
        self.gal_total = gal_total

    def toDict(self):
        return {
            "id": self.id,
            "sist_cria": self.sist_cria,
            "niv_terr": self.niv_terr,
            "cod_terr": self.cod_terr,
            "nom_terr": self.nom_terr,
            "cl_gal": self.cl_gal,
            "nom_cl_gal": self.nom_cl_gal,
            "gal_total": self.gal_total
        }


class GalinaceoSchema(Schema):
    sist_cria = fields.Str(required=True)
    niv_terr = fields.Str(required=True)
    cod_terr = fields.Str(allow_none=True)
    nom_terr = fields.Str(required=True)
    cl_gal = fields.Str(required=True)
    nom_cl_gal = fields.Str(required=True)
    gal_total = fields.Int(allow_none=True)

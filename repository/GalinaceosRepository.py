from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Galinaceos import Galinaceo

class GalinaceosRepository():
    def getAll(self, filtros: dict = None):
        stmt = select(Galinaceo)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getById(self, id):
        logger.info("Consultando galináceo pelo id.")
        return db.session.get(Galinaceo, id)

    def insert(self, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total):
        galinaceo = Galinaceo(None, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total)
        db.session.add(galinaceo)
        db.session.commit()
        logger.info(f"Galináceo inserido com id: {galinaceo.id}")
        return galinaceo

    def update(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total):
        galinaceo = db.session.get(Galinaceo, id)
        if galinaceo is None:
            return None
        galinaceo.sist_cria = sist_cria
        galinaceo.niv_terr = niv_terr
        galinaceo.cod_terr = cod_terr
        galinaceo.nom_terr = nom_terr
        galinaceo.cl_gal = cl_gal
        galinaceo.nom_cl_gal = nom_cl_gal
        galinaceo.gal_total = gal_total
        db.session.commit()
        return galinaceo

    def delete(self, id):
        galinaceo = db.session.get(Galinaceo, id)
        if galinaceo is None:
            return False
        db.session.delete(galinaceo)
        db.session.commit()
        return True

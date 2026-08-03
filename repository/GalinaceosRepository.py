from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Galinaceos import Galinaceo

class GalinaceosRepository():
    def getAll(self, filtros: dict = None):
        logger.info("Trazendo galinaceos")
        stmt = select(Galinaceo)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()
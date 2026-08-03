from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Galpao import Galpao

class GalpaoRepository():
    def getAll(self, filtros: dict = None):
        logger.info("Trazendo galpões")
        stmt = select(Galpao)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdGalpao(self, id):
        logger.info("Consultando galpão pelo id.")
        return db.session.get(Galpao, id)

    def insert(self, nome, capacidade, avicola_id):
        galpao = Galpao(None, nome, capacidade, avicola_id)
        db.session.add(galpao)
        db.session.commit()
        logger.info(f"Galpão inserido com id: {galpao.id}")
        return galpao
from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Avicola import Avicola

class AvicolaRepository():
    def getAll(self, filtros: dict = None):
        stmt = select(Avicola)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdAvicola(self, id):
        logger.info("Consultando avícola pelo id.")
        return db.session.get(Avicola, id)

    def insert(self, nome, tipo, capacidade):
        avicola = Avicola(None, nome, tipo, capacidade)
        db.session.add(avicola)
        db.session.commit()
        logger.info(f"Avícola inserida com id: {avicola.id}")
        return avicola

    def update(self, id, nome, tipo, capacidade):
        avicola = db.session.get(Avicola, id)
        if avicola is None:
            return None
        avicola.nome = nome
        avicola.tipo = tipo
        avicola.capacidade = capacidade
        db.session.commit()
        return avicola

    def delete(self, id):
        avicola = db.session.get(Avicola, id)
        if avicola is None:
            return False
        db.session.delete(avicola)
        db.session.commit()
        return True

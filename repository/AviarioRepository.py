from sqlalchemy import select
from helpers.database import db
from helpers.logger import logger
from models.Aviario import Aviario

class AviarioRepository():
    def getAll(self, filtros: dict = None):
        stmt = select(Aviario)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdAviario(self, id):
        logger.info("Consultando aviário pelo id.")
        return db.session.get(Aviario, id)

    def insert(self, nome, localizacao, capacidade):
        aviario = Aviario(None, nome, localizacao, capacidade)
        db.session.add(aviario)
        db.session.commit()
        logger.info(f"Aviário inserido com id: {aviario.id}")
        return aviario

    def update(self, id, nome, localizacao, capacidade):
        aviario = db.session.get(Aviario, id)
        if aviario is None:
            return None
        aviario.nome = nome
        aviario.localizacao = localizacao
        aviario.capacidade = capacidade
        db.session.commit()
        return aviario

    def delete(self, id):
        aviario = db.session.get(Aviario, id)
        if aviario is None:
            return False
        db.session.delete(aviario)
        db.session.commit()
        return True

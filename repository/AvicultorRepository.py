from sqlalchemy import select

from helpers.database import db
from helpers.logger import logger
from models.Avicultor import Avicultor

'''
  Manipulação do banco de dados para a entidade Avicultor.
'''


class AvicultorRepository():
    def getAll(self, filtros: dict = None):
        stmt = select(Avicultor)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def getByIdAvicultor(self, id):
        logger.info("Consultando avicultor pelo id.")
        return db.session.get(Avicultor, id)

    def insert(self, nome, nascimento, cpf, caf):
        avicultor = Avicultor(None, nome, nascimento, cpf, caf)
        db.session.add(avicultor)
        db.session.commit()
        logger.info(f"Avicultor inserido com id: {avicultor.id}")
        return avicultor

    def update(self, id, nome, nascimento, cpf, caf):
        avicultor = db.session.get(Avicultor, id)
        if avicultor is None:
            return None
        avicultor.nome = nome
        avicultor.nascimento = nascimento
        avicultor.cpf = cpf
        avicultor.caf = caf
        db.session.commit()
        return avicultor

    def delete(self, id):
        avicultor = db.session.get(Avicultor, id)
        if avicultor is None:
            return False
        db.session.delete(avicultor)
        db.session.commit()
        return True
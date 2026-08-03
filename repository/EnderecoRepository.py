from sqlalchemy import select

from helpers.database import db
from helpers.logger import logger
from models.Endereco import Endereco




class EnderecoRepository():
    def getAll(self, filtros: dict = None):
        logger.info("Trazendo endereços")
        stmt = select(Endereco)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    
    def insert(self, logradouro, cep, numero, avicultor_id):
        endereco = Endereco(logradouro, cep, numero, avicultor_id)
        db.session.add(endereco)
        db.session.commit()
        logger.info(f"Endereço inserido com id: {endereco.id}")
        return endereco
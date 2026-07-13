from helpers.logger import logger
from repository.GalinaceosRepository import GalinaceosRepository
from models.Galinaceos import Galinaceo

def rowToGalinaceo(row):
    return Galinaceo(
        row[0],  # id
        row[1],  # sist_cria
        row[2],  # niv_terr
        row[3],  # cod_terr
        row[4],  # nom_terr
        row[5],  # cl_gal
        row[6],  # nom_cl_gal
        row[7]   # gal_total
    )

class GalinaceosService:
    def __init__(self):
        self.repository = GalinaceosRepository()

    def getAll(self, filtros=None):
        rows = self.repository.getAll(filtros)
        logger.info(f"Serviço: Retornando {len(rows)} registros de galináceos com filtros: {filtros}")
        return [rowToGalinaceo(r) for r in rows]

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToGalinaceo(row) if row is not None else None

from models.Cl_Gal import Cl_Gal
from repository.Cl_GalRepository import Cl_GalRepository

def rowToCl_Gal(row):
    id = row[0]
    sigla = row[1]
    descricao = row[2]
    return Cl_Gal(id, sigla, descricao)

class Cl_GalService:
    def __init__(self):
        self.cl_galRepository = Cl_GalRepository()

    def getById(self, id):
        row = self.cl_galRepository.getById(id)
        return rowToCl_Gal(row) if row is not None else None

    def getAll(self):
        rows = self.cl_galRepository.getAll()
        return [rowToCl_Gal(r) for r in rows]

    def create(self, data):
        sigla = data["sigla"]
        descricao = data["descricao"]
        id = self.cl_galRepository.create(sigla, descricao)
        return Cl_Gal(id, sigla, descricao)

    def update(self, id, data):
        affected = self.cl_galRepository.update(id, data["sigla"], data["descricao"])
        if affected == 0:
            return None
        return Cl_Gal(id, data["sigla"], data["descricao"])

    def delete(self, id):
        affected = self.cl_galRepository.delete(id)
        return affected > 0

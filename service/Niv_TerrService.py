from models.Niv_Terr import Niv_Terr
from repository.Niv_TerrRepository import Niv_TerrRepository

def rowToNiv_Terr(row):
    id = row[0]
    nivel = row[1]
    descricao = row[2]
    return Niv_Terr(id, nivel, descricao)

class Niv_TerrService:
    def __init__(self):
        self.niv_terrRepository = Niv_TerrRepository()

    def getById(self, id):
        row = self.niv_terrRepository.getById(id)
        return rowToNiv_Terr(row) if row is not None else None

    def getAll(self):
        rows = self.niv_terrRepository.getAll()
        return [rowToNiv_Terr(r) for r in rows]

    def create(self, data):
        nivel = data["nivel"]
        descricao = data["descricao"]
        id = self.niv_terrRepository.create(nivel, descricao)
        return Niv_Terr(id, nivel, descricao)

    def update(self, id, data):
        affected = self.niv_terrRepository.update(id, data["nivel"], data["descricao"])
        if affected == 0:
            return None
        return Niv_Terr(id, data["nivel"], data["descricao"])

    def delete(self, id):
        affected = self.niv_terrRepository.delete(id)
        return affected > 0

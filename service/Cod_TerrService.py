from models.Cod_Terr import Cod_Terr
from repository.Cod_TerrRepository import Cod_TerrRepository

def rowToCod_Terr(row):
    id = row[0]
    codigo = row[1]
    descricao = row[2]
    return Cod_Terr(id, codigo, descricao)

class Cod_TerrService:
    def __init__(self):
        self.cod_terrRepository = Cod_TerrRepository()

    def getById(self, id):
        row = self.cod_terrRepository.getById(id)
        return rowToCod_Terr(row) if row is not None else None

    def getAll(self):
        rows = self.cod_terrRepository.getAll()
        return [rowToCod_Terr(r) for r in rows]

    def create(self, data):
        codigo = data["codigo"]
        descricao = data["descricao"]
        id = self.cod_terrRepository.create(codigo, descricao)
        return Cod_Terr(id, codigo, descricao)

    def update(self, id, data):
        affected = self.cod_terrRepository.update(id, data["codigo"], data["descricao"])
        if affected == 0:
            return None
        return Cod_Terr(id, data["codigo"], data["descricao"])

    def delete(self, id):
        affected = self.cod_terrRepository.delete(id)
        return affected > 0

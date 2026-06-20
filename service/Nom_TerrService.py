from models.Nom_Terr import Nom_Terr
from repository.Nom_TerrRepository import Nom_TerrRepository

def rowToNom_Terr(row):
    id = row[0]
    nome = row[1]
    descricao = row[2]
    return Nom_Terr(id, nome, descricao)

class Nom_TerrService:
    def __init__(self):
        self.nom_terrRepository = Nom_TerrRepository()

    def getById(self, id):
        row = self.nom_terrRepository.getById(id)
        return rowToNom_Terr(row) if row is not None else None

    def getAll(self):
        rows = self.nom_terrRepository.getAll()
        return [rowToNom_Terr(r) for r in rows]

    def create(self, data):
        nome = data["nome"]
        descricao = data["descricao"]
        id = self.nom_terrRepository.create(nome, descricao)
        return Nom_Terr(id, nome, descricao)

    def update(self, id, data):
        affected = self.nom_terrRepository.update(id, data["nome"], data["descricao"])
        if affected == 0:
            return None
        return Nom_Terr(id, data["nome"], data["descricao"])

    def delete(self, id):
        affected = self.nom_terrRepository.delete(id)
        return affected > 0

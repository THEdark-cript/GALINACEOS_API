from models.Sist_Cria import Sist_Cria
from repository.Sist_CriaRepository import Sist_CriaRepository



def rowToSist_Cria(row):
    id = row[0]
    sigla = row[1]
    descricao = row [2]
    return Sist_Cria(id, sigla, descricao)


class Sist_CriaService:
    def __init__(self):
        self.sist_criaRepository = Sist_CriaRepository()

    def getById(self, id):
        row = self.sist_criaRepository.getById(id)
        return rowToSist_Cria(row) if row is not None else None
    
    def getAll(self):
        rows = self.sist_criaRepository.getAll()
        return [rowToSist_Cria (r) for r in rows]
    
    def create(self, data):
        sigla = data ["sigla"]
        descricao = data ["descricao"]
        id = self.sist_criaRepository.create(sigla, descricao)
        return Sist_Cria(id, sigla, descricao)
    
    def update(self, id, data):
        affected = self.sist_criaRepository.update(id, data["sigla"], data["descricao"] )
        if affected ==0:
            return None
        return Sist_Cria(id, data["sigla"], data["descricao"])
    
    def delete (self, id):
        affected = self.sist_criaRepository.delete(id)
        return affected >0

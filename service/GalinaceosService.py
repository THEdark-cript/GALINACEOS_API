from models.Galinaceos import Galinaceos
from repository.GalinaceosRepository import GalinaceosRepository

def rowToGalinaceos(row):
    return Galinaceos(*row)

class GalinaceosService:
    def __init__(self):
        self.repository = GalinaceosRepository()

    def get_by_filters(self, filters):
        # Converter valores textuais em IDs
        if filters.get("sist_cria"):
            filters["sist_cria"] = self.repository.get_id("sist_cria", "sigla", filters["sist_cria"])
        if filters.get("niv_terr"):
            filters["niv_terr"] = self.repository.get_id("niv_terr", "sigla", filters["niv_terr"])
        if filters.get("cod_terr"):
            filters["cod_terr"] = self.repository.get_id("cod_terr", "codigo", filters["cod_terr"])
        if filters.get("nom_terr"):
            filters["nom_terr"] = self.repository.get_id("nom_terr", "nome", filters["nom_terr"])
        if filters.get("cl_gal"):
            filters["cl_gal"] = self.repository.get_id("cl_gal", "sigla", filters["cl_gal"])

        rows = self.repository.get_by_filters(filters)
        return [rowToGalinaceos(row) for row in rows]

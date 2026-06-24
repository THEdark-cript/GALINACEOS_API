from models.Galinaceos import Galinaceos
from repository.GalinaceosRepository import GalinaceosRepository

def rowToGalinaceos(row):
    return Galinaceos(*row)  

class GalinaceosService:
    def __init__(self):
        self.repository = GalinaceosRepository()

    def get_by_filters(self, filters):
        rows = self.repository.get_by_filters(filters)
        return [rowToGalinaceos(row) for row in rows]

from helpers.database import get_conn

class GalinaceosRepository:
    def get_by_filters(self, filters):
        conn = get_conn()
        cur = conn.cursor()

        query = "SELECT * FROM galinaceos WHERE 1=1"
        params = []

        if filters.get('sist_cria'):
            query += " AND sist_cria = %s"
            params.append(int(filters['sist_cria']))

        if filters.get('niv_terr'):
            query += " AND niv_terr = %s"
            params.append(int(filters['niv_terr']))

        if filters.get('cod_terr'):
            query += " AND cod_terr = %s"
            params.append(int(filters['cod_terr']))

        if filters.get('nom_terr'):
            query += " AND nom_terr = %s"
            params.append(filters['nom_terr'])

        if filters.get('cl_gal'):
            query += " AND cl_gal = %s"
            params.append(int(filters['cl_gal']))

        query += " LIMIT 100"

        try:
            cur.execute(query, params)
            rows = cur.fetchall()
            return rows
        finally:
            cur.close()

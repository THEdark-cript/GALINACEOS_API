from helpers.database import get_conn

class GalinaceosRepository:
    def get_id(self, table, column, value):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(f"SELECT id FROM {table} WHERE {column} = %s", (value,))
        row = cur.fetchone()
        cur.close()
        return row[0] if row else None

    def get_by_filters(self, filters):
        conn = get_conn()
        cur = conn.cursor()

        query = "SELECT * FROM galinaceos WHERE 1=1"
        params = []

        if filters.get('sist_cria'):
            query += " AND sist_cria = %s"
            params.append(filters['sist_cria'])
        if filters.get('niv_terr'):
            query += " AND niv_terr = %s"
            params.append(filters['niv_terr'])
        if filters.get('cod_terr'):
            query += " AND cod_terr = %s"
            params.append(filters['cod_terr'])
        if filters.get('nom_terr'):
            query += " AND nom_terr = %s"
            params.append(filters['nom_terr'])
        if filters.get('cl_gal'):
            query += " AND cl_gal = %s"
            params.append(filters['cl_gal'])

        query += " LIMIT 100"

        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
        return rows

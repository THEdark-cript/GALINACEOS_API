from helpers.database import get_conn

class Niv_TerrRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM niv_terr WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM niv_terr")
        return cursor.fetchall()

    def create(self, nivel, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO niv_terr(nivel, descricao) VALUES(%s, %s)", (nivel, descricao))
        conn.commit()
        return cursor.rowcount

    def update(self, id, nivel, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE niv_terr SET nivel=%s, descricao=%s WHERE id=%s", (nivel, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM niv_terr WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount

from helpers.database import get_conn

class Cod_TerrRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cod_terr WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cod_terr")
        return cursor.fetchall()

    def create(self, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cod_terr(codigo, descricao) VALUES(%s, %s)", (codigo, descricao))
        conn.commit()
        return cursor.rowcount

    def update(self, id, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE cod_terr SET codigo=%s, descricao=%s WHERE id=%s", (codigo, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cod_terr WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount

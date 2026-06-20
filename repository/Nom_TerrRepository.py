from helpers.database import get_conn

class Nom_TerrRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nom_terr WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nom_terr")
        return cursor.fetchall()

    def create(self, nome, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO nom_terr(nome, descricao) VALUES(%s, %s)", (nome, descricao))
        conn.commit()
        return cursor.rowcount

    def update(self, id, nome, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE nom_terr SET nome=%s, descricao=%s WHERE id=%s", (nome, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM nom_terr WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount

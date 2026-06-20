from helpers.database import get_conn

class Cl_GalRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cl_gal WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cl_gal")
        return cursor.fetchall()

    def create(self, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cl_gal(sigla, descricao) VALUES(%s, %s)", (sigla, descricao))
        conn.commit()
        return cursor.rowcount

    def update(self, id, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE cl_gal SET sigla=%s, descricao=%s WHERE id=%s", (sigla, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cl_gal WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount

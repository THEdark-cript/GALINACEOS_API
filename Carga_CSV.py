import pandas as pd
import numpy as np
import psycopg2
from psycopg2.extras import execute_values


conn = psycopg2.connect(
    dbname="galinaceos",
    user="postgres",
    password="123456",   
    host="localhost",
    port="5435"
)
cur = conn.cursor()


df = pd.read_csv("GALINACEOS.csv", sep=";", dtype=str)
df.replace({"X": np.nan, "": np.nan}, inplace=True)


if "NOM_CL_GAL" in df.columns:
    df.drop(columns=["NOM_CL_GAL"], inplace=True)


df.rename(columns={
    "SIST_CRIA": "sist_cria",
    "NIV_TERR": "niv_terr",
    "COD_TERR": "cod_terr",
    "NOM_TERR": "nom_terr",
    "CL_GAL": "cl_gal"
}, inplace=True)


def insert_unique(table, column, values):
    for v in values.unique():
        if pd.notna(v):
            cur.execute(f"INSERT INTO {table} ({column}) VALUES (%s) ON CONFLICT DO NOTHING;", (v,))
    conn.commit()

insert_unique("sist_cria", "sigla", df["sist_cria"])
insert_unique("niv_terr", "sigla", df["niv_terr"])
insert_unique("cod_terr", "codigo", df["cod_terr"])
insert_unique("nom_terr", "nome", df["nom_terr"])
insert_unique("cl_gal", "sigla", df["cl_gal"])


def build_map(table, column):
    cur.execute(f"SELECT id, {column} FROM {table};")
    rows = cur.fetchall()
    return {r[1]: r[0] for r in rows}

map_sist = build_map("sist_cria", "sigla")
map_niv = build_map("niv_terr", "sigla")
map_cod = build_map("cod_terr", "codigo")
map_nom = build_map("nom_terr", "nome")
map_cl = build_map("cl_gal", "sigla")


df["sist_cria"] = df["sist_cria"].map(map_sist)
df["niv_terr"] = df["niv_terr"].map(map_niv)
df["cod_terr"] = df["cod_terr"].map(map_cod)
df["nom_terr"] = df["nom_terr"].map(map_nom)
df["cl_gal"] = df["cl_gal"].map(map_cl)


for col in df.columns[5:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


values = [
    tuple(None if pd.isna(v) else (int(v) if isinstance(v, np.integer) else float(v) if isinstance(v, np.floating) else str(v))
          for v in row)
    for row in df.to_numpy()
]


cols = ",".join(df.columns)
insert_sql = f"INSERT INTO galinaceos ({cols}) VALUES %s"
execute_values(cur, insert_sql, values, page_size=1000)
conn.commit()

cur.close()
conn.close()

print("Carga concluída com sucesso!")

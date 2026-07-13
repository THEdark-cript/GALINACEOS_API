import pandas as pd
import numpy as np
from helpers.application import app
from helpers.database import get_conn

def extrair_e_carregar():
    print("Lendo o arquivo GALINACEOS.csv com Pandas")

    # Lê o CSV com separador ';' e mantém tudo como string inicialmente
    df = pd.read_csv('GALINACEOS.csv', sep=';', dtype=str, keep_default_na=False)

    # Substitui valores vazios ou 'X' por NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.replace('X', np.nan)

    # Remove pontos de separação de milhares em GAL_TOTAL
    if 'GAL_TOTAL' in df.columns:
        df['GAL_TOTAL'] = df['GAL_TOTAL'].str.replace('.', '', regex=False)

    with app.app_context():
        conn = get_conn()
        cursor = conn.cursor()

        print("Removendo duplicatas")
        cursor.execute("TRUNCATE TABLE galinaceos RESTART IDENTITY;")

        print("Colocando dados no postgres")
        query_insert = """
            INSERT INTO galinaceos (sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        inseridos = 0
        for _, row in df.iterrows():
            gal_total_val = None
            if pd.notna(row['GAL_TOTAL']):
                try:
                    gal_total_val = int(row['GAL_TOTAL'])
                except ValueError:
                    gal_total_val = None

            valores = (
                str(row['SIST_CRIA']) if pd.notna(row['SIST_CRIA']) else None,
                str(row['NIV_TERR']) if pd.notna(row['NIV_TERR']) else None,
                str(row['COD_TERR']) if pd.notna(row['COD_TERR']) else None,
                str(row['NOM_TERR']) if pd.notna(row['NOM_TERR']) else None,
                str(row['CL_GAL']) if pd.notna(row['CL_GAL']) else None,
                str(row['NOM_CL_GAL']) if pd.notna(row['NOM_CL_GAL']) else None,
                gal_total_val
            )

            cursor.execute(query_insert, valores)
            inseridos += 1

        conn.commit()
        cursor.close()
        print(f"Sucesso total! {inseridos} registros Carregados no banco com sucesso...")

if __name__ == "__main__":
    extrair_e_carregar()

DROP TABLE IF EXISTS galinaceos;
-- Tabela de galinaceos
CREATE TABLE IF NOT EXISTS galinaceos (
    id SERIAL PRIMARY KEY,
    sist_cria VARCHAR(100),  
    niv_terr VARCHAR(50),     
    cod_terr VARCHAR(50),    
    nom_terr VARCHAR(150),    
    cl_gal VARCHAR(50),       
    nom_cl_gal VARCHAR(150),  
    gal_total BIGINT          
);

-- Tabela de avicultores
CREATE TABLE IF NOT EXISTS tb_avicultor(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
);

-- Tabela de endereços
CREATE TABLE IF NOT EXISTS tb_endereco(
    id SERIAL PRIMARY KEY,
    logradouro TEXT,
    cep VARCHAR(8) NOT NULL,
    numero INTEGER,
    avicultor_id INTEGER NOT NULL REFERENCES tb_avicultor(id)
);
-- SISTEMA DE CRIAÇÃO
CREATE TABLE sist_cria (
    id SERIAL PRIMARY KEY,
    sigla VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

-- NÍVEL TERRITORIAL
CREATE TABLE niv_terr (
    id SERIAL PRIMARY KEY,
    sigla VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

-- CÓDIGO TERRITORIAL
CREATE TABLE cod_terr (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

-- NOME TERRITORIAL
CREATE TABLE nom_terr (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

-- CABEÇA GALINACEO
CREATE TABLE cl_gal (
    id SERIAL PRIMARY KEY,
    sigla VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

--  GALINACEOS
CREATE TABLE galinaceos (
    id SERIAL PRIMARY KEY,
    sist_cria INT REFERENCES sist_cria(id),
    niv_terr INT REFERENCES niv_terr(id),
    cod_terr INT REFERENCES cod_terr(id),
    nom_terr INT REFERENCES nom_terr(id),
    cl_gal INT REFERENCES cl_gal(id),
    e_cria_gal BIGINT,
    e_tem_gal BIGINT,
    e_gal_vend BIGINT,
    e_ovos_prod BIGINT,
    e_ovos_vend BIGINT,
    e_subs BIGINT,
    e_comerc BIGINT,
    e_recebe_ori BIGINT,
    e_ori_gov BIGINT,
    e_ori_propria BIGINT,
    e_ori_coop BIGINT,
    e_ori_emp_int BIGINT,
    e_ori_emp_priv BIGINT,
    e_ori_ong BIGINT,
    e_ori_sist_s BIGINT,
    e_ori_outra BIGINT,
    e_gal_eng BIGINT,
    e_gal_galos BIGINT,
    e_gal_poed BIGINT,
    e_gal_matr BIGINT,
    e_assoc_coop BIGINT,
    e_financ BIGINT,
    e_financ_coop BIGINT,
    e_financ_integ BIGINT,
    e_dap BIGINT,
    e_agrifam BIGINT,
    e_n_agrifam BIGINT,
    e_produtor BIGINT,
    e_cooperativa BIGINT,
    e_sa_ldta BIGINT,
    e_cnpj BIGINT,
    gal_total BIGINT,
    gal_eng BIGINT,
    gal_galos BIGINT,
    gal_poed BIGINT,
    gal_matr BIGINT,
    gal_vend BIGINT,
    v_gal_vend NUMERIC(20,2),
    q_dz_prod BIGINT,
    q_dz_vend BIGINT,
    v_q_dz_prod NUMERIC(20,2),
    v_q_dz_vend NUMERIC(20,2),
    a_total BIGINT,
    a_past_plant BIGINT,
    a_lav_perm BIGINT,
    a_lav_temp BIGINT,
    a_apprl BIGINT,
    vtp_agro NUMERIC(20,2),
    rect_agro NUMERIC(20,2),
    n_trab_total BIGINT,
    n_trab_lacos BIGINT
);

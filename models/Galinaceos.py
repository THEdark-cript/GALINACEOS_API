class Galinaceos:
    def __init__(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal,
                 e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend,
                 e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria,
                 e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong,
                 e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed,
                 e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ,
                 e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa,
                 e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed,
                 gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend,
                 v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm,
                 a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total,
                 n_trab_lacos):
        self.id = id
        self.sist_cria = sist_cria
        self.niv_terr = niv_terr
        self.cod_terr = cod_terr
        self.nom_terr = nom_terr
        self.cl_gal = cl_gal
        self.e_cria_gal = e_cria_gal
        self.e_tem_gal = e_tem_gal
        self.e_gal_vend = e_gal_vend
        self.e_ovos_prod = e_ovos_prod
        self.e_ovos_vend = e_ovos_vend
        self.e_subs = e_subs
        self.e_comerc = e_comerc
        self.e_recebe_ori = e_recebe_ori
        self.e_ori_gov = e_ori_gov
        self.e_ori_propria = e_ori_propria
        self.e_ori_coop = e_ori_coop
        self.e_ori_emp_int = e_ori_emp_int
        self.e_ori_emp_priv = e_ori_emp_priv
        self.e_ori_ong = e_ori_ong
        self.e_ori_sist_s = e_ori_sist_s
        self.e_ori_outra = e_ori_outra
        self.e_gal_eng = e_gal_eng
        self.e_gal_galos = e_gal_galos
        self.e_gal_poed = e_gal_poed
        self.e_gal_matr = e_gal_matr
        self.e_assoc_coop = e_assoc_coop
        self.e_financ = e_financ
        self.e_financ_coop = e_financ_coop
        self.e_financ_integ = e_financ_integ
        self.e_dap = e_dap
        self.e_agrifam = e_agrifam
        self.e_n_agrifam = e_n_agrifam
        self.e_produtor = e_produtor
        self.e_cooperativa = e_cooperativa
        self.e_sa_ldta = e_sa_ldta
        self.e_cnpj = e_cnpj
        self.gal_total = gal_total
        self.gal_eng = gal_eng
        self.gal_galos = gal_galos
        self.gal_poed = gal_poed
        self.gal_matr = gal_matr
        self.gal_vend = gal_vend
        self.v_gal_vend = v_gal_vend
        self.q_dz_prod = q_dz_prod
        self.q_dz_vend = q_dz_vend
        self.v_q_dz_prod = v_q_dz_prod
        self.v_q_dz_vend = v_q_dz_vend
        self.a_total = a_total
        self.a_past_plant = a_past_plant
        self.a_lav_perm = a_lav_perm
        self.a_lav_temp = a_lav_temp
        self.a_apprl = a_apprl
        self.vtp_agro = vtp_agro
        self.rect_agro = rect_agro
        self.n_trab_total = n_trab_total
        self.n_trab_lacos = n_trab_lacos

    def toDict(self):
        return {c: getattr(self, c) for c in self.__dict__ if not c.startswith("_")}

from flask import Blueprint, request, jsonify
from service.GalinaceosService import GalinaceosService

galinaceos_bp = Blueprint('galinaceos', __name__, url_prefix='/galinaceos')
service = GalinaceosService()

@galinaceos_bp.get("/")
def get_galinaceos():
    try:
        filters = {}

        if request.args.get('SIST_CRIA'):
            filters['sist_cria'] = request.args.get('SIST_CRIA')
        if request.args.get('NIV_TERR'):
            filters['niv_terr'] = request.args.get('NIV_TERR')
        if request.args.get('COD_TERR'):
            filters['cod_terr'] = request.args.get('COD_TERR')
        if request.args.get('NOM_TERR'):
            filters['nom_terr'] = request.args.get('NOM_TERR')
        if request.args.get('CL_GAL'):
            filters['cl_gal'] = request.args.get('CL_GAL')

        galinaceos = service.get_by_filters(filters)
        resultado = [g.toDict() for g in galinaceos]

        return jsonify({
            'total': len(resultado),
            'dados': resultado
        }), 200

    except Exception as e:
        return jsonify({'erro': 'Erro ao buscar dados', 'detalhes': str(e)}), 500

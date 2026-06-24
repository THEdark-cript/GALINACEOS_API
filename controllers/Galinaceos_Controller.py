from flask import Blueprint, request, jsonify
from service.GalinaceosService import GalinaceosService

galinaceos_bp = Blueprint('galinaceos', __name__, url_prefix='/galinaceos')
service = GalinaceosService()

@galinaceos_bp.get("/")
def get_galinaceos():
    try:
        filters = {}

        if request.args.get('sist_cria'):
            filters['sist_cria'] = request.args.get('sist_cria')
        if request.args.get('niv_terr'):
            filters['niv_terr'] = request.args.get('niv_terr')
        if request.args.get('cod_terr'):
            filters['cod_terr'] = request.args.get('cod_terr')
        if request.args.get('nom_terr'):
            filters['nom_terr'] = request.args.get('nom_terr')
        if request.args.get('cl_gal'):
            filters['cl_gal'] = request.args.get('cl_gal')

        galinaceos = service.get_by_filters(filters)
        resultado = [g.toDict() for g in galinaceos]

        return jsonify({
            'total': len(resultado),
            'dados': resultado
        }), 200

    except Exception as e:
        return jsonify({'erro': 'Erro ao buscar dados', 'detalhes': str(e)}), 500

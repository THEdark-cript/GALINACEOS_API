from helpers.application import app
from controllers.Sist_CriaController import sist_cria_bp
from controllers.Nom_TerrController import nom_terr_bp
from controllers.Niv_TerrController import niv_terr_bp
from controllers.Cod_TerrController import cod_terr_bp
from controllers.Cl_GalController import cl_gal_bp
from controllers.Galinaceos_Controller import galinaceos_bp 



@app.get("/")
def index():
    return "{'versão':'0.5.0'}", 200


@app.get("/health")
def healthCheck():
    return {"online": "True"}, 200


app.register_blueprint(sist_cria_bp)
app.register_blueprint(nom_terr_bp)
app.register_blueprint(niv_terr_bp)
app.register_blueprint(cod_terr_bp)
app.register_blueprint(cl_gal_bp)
app.register_blueprint(galinaceos_bp)
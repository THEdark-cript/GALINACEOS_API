from helpers.application import app, api
from helpers.database import db

# Controllers RESTful
from controllers.AvicultorController import AvicultoresController, AvicultorController

from controllers.EnderecoController import EnderecosController, EnderecoController

from controllers.IndexController import IndexController, HealthController

from controllers.AvicolaController import AvicolasController,AvicolaController

from controllers.AviarioController import AviariosController, AviarioController

from controllers.GalpaoController import GalpoesController, GalpaoController

from controllers.Galinaceos_Controller import galinaceos_bp



api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')


api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")

api.add_resource(EnderecosController, "/enderecos")
api.add_resource(EnderecoController, "/enderecos/<int:endereco_id>")

api.add_resource(AvicolasController, "/avicolas")
api.add_resource(AvicolaController, "/avicolas/<int:avicola_id>")

api.add_resource(AviariosController, "/aviarios")
api.add_resource(AviarioController, "/aviarios/<int:aviario_id>")

api.add_resource(GalpoesController, "/galpoes")
api.add_resource(GalpaoController, "/galpoes/<int:galpao_id>")

app.register_blueprint(galinaceos_bp)

with app.app_context():
    db.create_all()
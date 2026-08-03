from helpers.application import app, api
from helpers.database import db

# Controllers RESTful
from controllers.AvicultorController import AvicultoresController, AvicultorController

from controllers.EnderecoController import EnderecosController

from controllers.IndexController import IndexController, HealthController

from controllers.AvicolaController import AvicolasController,AvicolaController

from controllers.GalpaoController import GalpoesController, GalpaoController

from controllers.Galinaceos_Controller import GalinaceosController



api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')


api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")

api.add_resource(EnderecosController, "/enderecos")

api.add_resource(AvicolasController, "/avicola")
api.add_resource(AvicolaController, "/avicola/<int:avicola_id>")


api.add_resource(GalpoesController, "/galpoes")
api.add_resource(GalpaoController, "/galpoes/<int:galpao_id>")

api.add_resource(GalinaceosController, "/galinaceos")

with app.app_context():
    db.create_all()
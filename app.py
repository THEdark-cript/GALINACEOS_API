from helpers.application import app, api
from helpers.database import db

# Controllers RESTful
from controllers.AvicultorController import AvicultoresController, AvicultorController
from controllers.EnderecoController import EnderecosController, EnderecoController
from controllers.IndexController import IndexController, HealthController
from controllers.Galinaceos_Controller import galinaceos_bp



api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')


api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")

api.add_resource(EnderecosController, "/enderecos")
api.add_resource(EnderecoController, "/enderecos/<int:endereco_id>")

app.register_blueprint(galinaceos_bp)

with app.app_context():
    db.create_all()
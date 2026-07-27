from helpers.application import app
from controllers.Galinaceos_Controller import galinaceos_bp 



@app.get("/")
def index():
    return "{'versão':'0.5.0'}", 200


@app.get("/health")
def healthCheck():
    return {"online": "True"}, 200


app.register_blueprint(galinaceos_bp)
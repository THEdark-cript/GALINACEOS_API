from dotenv import load_dotenv
from flask import Flask

from helpers.cors import cors



app = Flask(__name__)
cors.init_app(app)
load_dotenv()

from flask import Flask
from connexion.resolver import RestyResolver
import connexion
from flask import request

#app = Flask(__name__)
app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('AV_api.yaml', resolver=RestyResolver('app'))
#app.run(port="9090")


from app import views
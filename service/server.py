import os
import logging

from flask import Flask
from flask_restful import Api
from waitress import serve

from resources.index import IndexResource
from resources.model import ModelResource

from settings import *


app = Flask(__name__)
app.logger.setLevel(LOGGING__LOG_LEVEL)
api = Api(app)

api.add_resource(IndexResource, "/")
api.add_resource(ModelResource, "/model")


if __name__ == "__main__":
    if SERVICE__DEBUG:
        app.run(host=SERVICE__HOST, 
                port=SERVICE__PORT, 
                debug=SERVICE__DEBUG)
    else:
        serve(
            app, host=SERVICE__HOST, 
                 port=SERVICE__PORT
        )
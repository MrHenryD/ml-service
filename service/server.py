import os
import logging

from flask import Flask
from flask_restful import Api
from waitress import serve

from resources.index import IndexResource
from resources.model import ModelResource

from settings import *


app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
api = Api(app)

api.add_resource(IndexResource, '/')
api.add_resource(ModelResource, '/model')

if __name__ == '__main__':
    if DEBUG:        
        app.run(host=HOST, port=PORT, debug=DEBUG)
    else:
        serve(
            app, host=HOST, port=PORT
        )
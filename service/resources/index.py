import logging

from flask_restful import Resource, Api


logger = logging.getLogger(__name__)

class IndexResource(Resource):
    def get(self):
        return {
            "endpoints": {
                "index": "/",
                "model": "/model"        
            }
        }
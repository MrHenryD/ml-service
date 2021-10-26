import logging
from typing import Dict, Literal

from flask import request
from flask_restful import Resource, Api


logger = logging.getLogger(__name__)

class ModelResource(Resource):

    @staticmethod
    def _predict(age: int, sqft: int, bedrooms: int, washrooms: int, country: Literal["US", "MX", "CA"], **kwargs) -> Dict:
        return {
            "price": (int(bedrooms) + int(washrooms)) * 120609,
            "sqft": sqft,
            "bedrooms": bedrooms,
            "washrooms": washrooms,
            "country": country,
        }

    def get(self) -> Dict:
        return {
            "model": True,
            "lastUpdated": "2021-09-02 10:39:33"
        }

    def post(self) -> Dict:
        payload = request.args
        prediction = self._predict(**payload)
        return prediction
        

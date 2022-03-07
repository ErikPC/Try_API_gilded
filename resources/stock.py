from flask_restful import Resource
from repository.repository import DB_atlas


class Stock(Resource):
    def get(self):
        return DB_atlas.get_stock()

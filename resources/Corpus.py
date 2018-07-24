from datetime import datetime

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sqlalchemy.sql.functions import now

from models.CorpusModel import CorpusModel


class Corpus(Resource):
    TABLE_NAME = 'corpus'

    def get(self, corpus_id):
        corpus = CorpusModel.find_by_id(corpus_id)
        if corpus:
            return corpus.json()
        return {'message': 'Corpus not found'}, 404


class CorpusList(Resource):
    def get(self):
        return {'corpora': list(map(lambda x: x.json(), CorpusModel.query.all()))}

    @jwt_required()
    def post(self):
        corpus = CorpusModel()

        try:
            corpus.save_to_db()
        except:
            return {'message': 'An error occurred inserting the corpus'}, 500

        return corpus.json(), 201

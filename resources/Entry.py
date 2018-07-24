from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sqlalchemy.sql.functions import now

from models.CorpusModel import CorpusModel
from models.EntryModel import EntryModel


class CorpusEntry(Resource):
    TABLE_NAME = 'entry'
    parser = reqparse.RequestParser()
    parser.add_argument('author',
                        type=str,
                        required=True,
                        help='Author of this entry')
    parser.add_argument('entry',
                        type=str,
                        required=True,
                        help='The body of text of the entry')
    parser.add_argument('entry_start',
                        type=str,
                        required=False,
                        default=now(),
                        help='Start time of this entry')
    parser.add_argument('entry_end',
                        type=str,
                        required=False,
                        default=now(),
                        help='End time of this entry')

    def get(self, corpusId, entryId):
        corpus = CorpusModel.find_by_id(corpusId)
        if not corpus:
            return {'message': 'No such corpus found'}, 404

        entry = EntryModel.find_by_id(entryId)
        if entry:
            return entry.json()
        return {'message': 'Entry not found'}, 404


class EntryList(Resource):
    def get(self, corpusId):
        resp = {'entries': list(map(lambda x: x.json(), EntryModel.find_by_corpus_id(corpusId)))}
        if not resp['entries']:
            return {'message': 'Corpus not found'}, 404
        return resp

    @jwt_required()
    def post(self, corpusId):
        data = CorpusEntry.parser.parse_args()

        corpus = CorpusModel.find_by_id(corpusId)
        if not corpus:
            return {'message': 'No such entry found'}, 404

        entry = EntryModel(corpusId, data['author'], data['entry'], data['entry_start'], data['entry_end'])

        from pprint import pprint
        print(entry.json())

        try:
            entry.save_to_db()
        except:
            return {'message': 'An error occurred inserting the entry'}, 500

        return entry.json(), 201

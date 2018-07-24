from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from db import db
from resources.Corpus import Corpus, CorpusList
from resources.Entry import CorpusEntry, EntryList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Very secret password.'
app.url_map.strict_slashes = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(CorpusList, '/corpora')
api.add_resource(Corpus, '/corpora/<int:corpus_id>')
api.add_resource(EntryList, '/corpora/<int:corpusId>/entries')
api.add_resource(CorpusEntry, '/corpora/<int:corpusId>/entries/<int:entryId>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)

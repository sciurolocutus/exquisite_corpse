from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects.sqlite import DATETIME

from db import db

class EntryModel(db.Model):
    __tablename__ = 'entry'

    id = db.Column('entry_id', db.Integer, primary_key=True)
    corpus_id = db.Column('corpus_id', db.Integer, db.ForeignKey('corpus.corpus_id'))
    corpus = db.relationship('CorpusModel')

    author = db.Column(db.String(32), nullable=False)
    entry = db.Column(db.String(1024))
    entry_start = db.Column(DATETIME, nullable=False, default=func.now())
    entry_end = db.Column(DATETIME, default=func.now())

    def __init__(self, corpus_id, author, entry, entry_start, entry_end):
        self.corpus_id = corpus_id
        self.author = author
        self.entry = entry

        if isinstance(entry_start, datetime):
            self.entry_start = entry_start
        elif isinstance(entry_start, str):
            self.entry_start = datetime.strptime(entry_start, '%Y-%m-%d %H:%M')

        if isinstance(entry_end, datetime):
            self.entry_end = entry_end
        elif isinstance(entry_end, str):
            self.entry_end = datetime.strptime(entry_end, '%Y-%m-%d %H:%M')

    def json(self):
        return {
            'id': self.id,
            'corpus_id': self.corpus_id,
            'author': self.author,
            'entry': self.entry,
            'entry_start': self.entry_start.replace(microsecond=0).isoformat() if self.entry_start else datetime.now().replace(microsecond=0).isoformat(),
            'entry_end':  self.entry_end.replace(microsecond=0).isoformat() if self.entry_end else datetime.now().replace(microsecond=0).isoformat()
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_corpus_id(cls, _corpus_id):
        return cls.query.filter_by(corpus_id=_corpus_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

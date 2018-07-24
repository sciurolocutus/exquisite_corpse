from sqlalchemy.orm import relationship

from db import db


class CorpusModel(db.Model):
    __tablename__ = 'corpus'

    id = db.Column('corpus_id', db.Integer, primary_key=True)

    from models.EntryModel import EntryModel
    entries = relationship('EntryModel', lazy='dynamic')

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'entries': [entry.json() for entry in self.entries.all()]
        }

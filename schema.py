from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, func, ForeignKey

metadata = MetaData()

corpus = Table('corpus', metadata,
               Column('corpus_id', Integer,
                      primary_key=True),
               Column('original_author', String(32), nullable=False),
               Column('final_author', String(32)),
               Column('entry_start', DateTime, nullable=False, default=func.now()),
               Column('entry_end', DateTime, nullable=False, default=func.now())
               )

entry = Table('entry', metadata,
              Column('entry_id', Integer,
                     primary_key=True),
              Column('corpus_id', Integer, ForeignKey('corpus.corpus_id')),
              Column('author', String(32), nullable=False),
              Column('entry', String(1024)),
              Column('entry_start', DateTime, nullable=False, default=func.now()),
              Column('entry_end', DateTime, default=func.now())
              )
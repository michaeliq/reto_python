import db
from sqlalchemy import Column, Integer, String

class Keyword(db.Base):
    __tablename__= 'keyword'

    id = Column(Integer,primary_key=True)
    keyword_ = Column(String,nullable=False)
    position = Column(Integer)

    def __init__(self,keyword,position=0):
        self.keyword_=keyword
        self.position=position

    def __repr__(self):
        return f'{self.keyword_}'

    def __str__(self):
        return self.keyword_
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_reg(self,position):
        item = db.session.query(Keyword).get(self.id)
        item.position = position
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def get_all():
        return db.session.query(Keyword).all()

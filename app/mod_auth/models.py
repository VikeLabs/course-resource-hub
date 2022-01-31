from app import db

class Base(db.Model):
    # Abstract model for inheritence
    __abstract__  = True
    # TODO initialize base model with id and timestamp? maybe

    # Do:
    # class Name(Base):
    #   __tablename__ = 'name'

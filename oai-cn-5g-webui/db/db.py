from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DB():
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)

    def query(self, model, **filters):
        session = self.Session()
        try:
            result = session.query(model).filter_by(**filters).all()
            return result
        finally:
            session.close()

    def insert(self, instance):
        session = self.Session()
        try:
            session.add(instance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    def update(self, model, filters, data):
        session = self.Session()
        try:
            instances = session.query(model).filter_by(**filters).all()
            for instance in instances:
                for key, value in data.items():
                    setattr(instance, key, value)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

    def delete(self, model, **filters):
        session = self.Session()
        try:
            instances = session.query(model).filter_by(**filters).all()
            for instance in instances:
                session.delete(instance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

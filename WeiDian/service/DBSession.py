# *- coding:utf8 *-
import sys
import os

from test.base_model import Query

sys.path.append(os.path.dirname(os.getcwd()))
from sqlalchemy.orm import sessionmaker
from WeiDian.models import model

# db_session = sessionmaker(bind=model.mysql_engine, query_cls=Query)
db_session = sessionmaker(bind=model.mysql_engine)

def get_session():
    try:
        session = db_session()
        status = True
    except Exception as e:
        print e.message
        session = None
        status = False
    finally:
        return session, status

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

url = f'sqlite:///alchemy.db'
engine = create_engine(url, echo=False)
Base = declarative_base()
# engine.execute('alter table user_account add column gender String(10)')
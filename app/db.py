from sqlalchemy import Table, create_engine, MetaData
from APP import app

db_engine = create_engine(app.config['DB_URI'])
db_metadata = MetaData(bind=db_engine)

#User        = Table('user', db_metadata, autoload=True)


import os
SECRET_KEY = os.getenv("SECRET")
SQLALCHEMY_DATABASE_URI = os.getenv("PSQL_LINK")
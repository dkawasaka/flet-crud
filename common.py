from pydal import DAL, Field
from settings import DB_URI, T_FOLDER, DB_FOLDER, DB_POOL_SIZE, DB_MIGRATE, DB_FAKE_MIGRATE
from pluralize import Translator

db = DAL(
    DB_URI,
    folder=DB_FOLDER,
    pool_size=DB_POOL_SIZE,
    migrate=DB_MIGRATE,
    fake_migrate=DB_FAKE_MIGRATE,
)

T = Translator(T_FOLDER)

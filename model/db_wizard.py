import uuid

from common import db, Field, T
from settings import DB_MIGRATE

User = db.define_table('auth_user',
        Field('uuid',       length=64,  default=lambda:str(uuid.uuid4()),   writable=False,	readable=False),
        Field('username',   type='string', required=True, unique=True),
        Field('password',   type='string', required=True),
        migrate=DB_MIGRATE
        )

db.commit()
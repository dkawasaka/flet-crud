import uuid

from common import db, Field, T
from settings import DB_MIGRATE

User = db.define_table('auth_user',
        Field('uuid',       length=64,  default=lambda:str(uuid.uuid4()),   writable=False,	readable=False),
        Field('username',   type='string', required=True, unique=True),
        Field('password',   type='string', required=True),
        migrate=DB_MIGRATE
        )

Funcionar = db.define_table('funcionarios',
        Field('uuid',       length=64,  default=lambda:str(uuid.uuid4()),   writable=False,	readable=False),
        Field('nome', type='string', required=True, notnull=True),
        Field('cargo', type='string', length=50),
        Field('departamento', type='string', length=50),
        Field('email', type='string', length=180),
        Field('is_active', type='boolean', default=True, required=True, notnull=True),
        migrate=DB_MIGRATE
)

db.commit()
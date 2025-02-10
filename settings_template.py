# Configuração do banco de dados
import os

def required_folder(*parts):
    """joins the args and creates the folder if not exists"""
    path = os.path.join(*parts)
    if not os.path.exists(path):
        os.makedirs(path)
    assert os.path.isdir(path), f"{path} is not a folder as required"
    return path

APP_FOLDER = os.path.dirname(__file__)
APP_NAME = os.path.split(APP_FOLDER)[-1]
DB_FOLDER = required_folder(APP_FOLDER, "databases")

DB_URI = "mysql://user:password@host:port/banco?set_encoding=utf8mb4"
DB_POOL_SIZE = 1
DB_MIGRATE = True
DB_FAKE_MIGRATE = False  # maybe?

T_FOLDER = required_folder(APP_FOLDER, "translations")

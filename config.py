from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DATABASE = environ.get('DATABASE')


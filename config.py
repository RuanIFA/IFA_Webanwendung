#Eigenentwicklung
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ruan$ifa'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ruan:ruan$ifa@localhost/luxury_rents'
    SQLALCHEMY_TRACK_MODIFICATIONS = False




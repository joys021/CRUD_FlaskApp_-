# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:37:34 2020
defines the basic config that did in main.py and
then adds environment-specific configuration on the top

@author: joy
"""


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = <Production DB URL>
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = <Development DB URL>
    SQLALCHEMY_ECHO = False
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = <Testing DB URL>
    SQLALCHEMY_ECHO = False
    
    
    
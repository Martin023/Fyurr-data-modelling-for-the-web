class Config:
   
    SQLALCHEMY_DATABASE_URI = 'postgresql://martin023:0000@localhost/fyyur_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'my_key'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://martin023:0000@localhost/fyyur_app'
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)



class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/fyyur_app'


  

class DevConfig(Config):
    DEBUG = True


    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
    
}
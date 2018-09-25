class Config:
    pass

class Development(Config):
    DEBUG=True
    TESTING=False

class Testing(Config):
    DEBUG=True
    TESTING=True

class Production(Config):
    pass


app_config={
    "development":Development,
    "testing":Testing,
    "production":Production,
    "default":Development
}
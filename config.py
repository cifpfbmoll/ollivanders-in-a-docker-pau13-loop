class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "secret_key"

    DB_NAME = "ollivanders"
    DB_USERNAME = "root"
    DB_PASSWORD = "power2021"

    # UPLOADS = ""

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    # DEBUG = False
    # TESTING = False

    # SECRET_KEY = "secret_key"

    # DB_NAME = "ollivanders"
    # DB_USERNAME = "root"
    # DB_PASSWORD = "power2021"
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    # SECRET_KEY = "secret_key"

    DB_NAME = "ollivanders"
    DB_USERNAME = "root"
    DB_PASSWORD = "power2021"

    SESSION_COOKIE_SECURE = False


class TestingtConfig(Config):
    TESTING = True

    # SECRET_KEY = "secret_key"

    DB_NAME = "ollivanders"
    DB_USERNAME = "root"
    DB_PASSWORD = "power2021"

    SESSION_COOKIE_SECURE = False

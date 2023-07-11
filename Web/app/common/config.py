import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # DB_USERNAME : str = os.getenv("DB_USERNAME")
    # DB_PASSWORD = os.getenv("DB_PASSWROD")
    # DB_HOST : str = os.getenv("DB_HOST", "localhost")
    # DB_PORT : str = os.getenv("DB_PORT", 3306)
    # DB_DATABASE : str = os.getenv("DB_DATABASE")

    DB_USERNAME = "kist"
    DB_PASSWORD = "kist"
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_DATABASE = "kist"

    DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"


settings = Settings()
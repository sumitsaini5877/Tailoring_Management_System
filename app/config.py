# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # 👈 loads .env automatically

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///tailoring.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

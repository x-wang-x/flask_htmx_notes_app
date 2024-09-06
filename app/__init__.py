from flask import Flask
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

app = Flask(__name__)
app.config.update(
    SECRET_KEY = os.getenv('SECRET_KEY','abc123')
)

def create_connection(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row
    return conn
from app.models import init_db
init_db(create_connection(os.getenv('DB_NAME','app.db')))
from app import routes


import sqlite3

from flask import Flask
from flask_restx import Resource, fields, Api


app: Flask = Flask(__name__)
# app.py

# Required imports
import random
import os
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

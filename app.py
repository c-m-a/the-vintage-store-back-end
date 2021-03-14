# app.py

# Required imports
import random
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app)

# Range of products to randomize
MIN = 1
MAX = 3

# Initialize Firestore DB
cred        = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db          = firestore.client()
product_ref = db.collection('products')
order_ref   = db.collection('orders')

@app.route('/products', methods=['GET'])
@cross_origin()
def get_product():
    """
        read() : Fetches documents from Firestore collection as JSON.
        product : Return document that matches query ID.
        all_products : Return all documents.
    """
    try:
        product_id = str(random.randrange(MIN, MAX))
        product = product_ref.document(product_id).get()
        return jsonify(product.to_dict()), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/orders', methods=['POST'])
@cross_origin()
def create_order():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
    """
    try:
        now = datetime.now()
        id = int(datetime.timestamp(now))
        id = str(id)
        order_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


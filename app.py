# app.py

# Required imports
import random
import os
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

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)


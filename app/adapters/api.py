from flask import Flask, jsonify
from app.application.services import ProductService
from app.infrastructure.repository import ProductRepository

app = Flask(__name__)

repository = ProductRepository()
service = ProductService(repository=repository)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = service.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict())
    else:
        return jsonify({'error': 'Product not found'}), 404

from app.infrastructure.repository import ProductRepository

class ProductService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product_by_id(self, product_id):
        return self.repository.find_by_id(product_id)
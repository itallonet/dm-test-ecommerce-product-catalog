import pytest
from app.application.services import ProductService
from app.infrastructure.repository import ProductRepository

# Mock de ProductRepository
class MockRepository(ProductRepository):
    def __init__(self, products):
        self.products = products

    def find_by_id(self, product_id):
        return self.products.get(product_id, None)

@pytest.fixture
def product_service():
    products = {1: {'id': 1, 'name': 'Test Product', 'description': 'A test product', 'price': 19.99}}
    repository = MockRepository(products)
    return ProductService(repository)

def test_get_product_by_id(product_service):
    product = product_service.get_product_by_id(1)
    assert product is not None
    assert product['id'] == 1
    assert product['name'] == 'Test Product'

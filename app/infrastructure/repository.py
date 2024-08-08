from app.infrastructure.database import get_db, get_db_cursor
from app.domain.product import Product

class ProductRepository:
    def find_by_id(self, product_id):
        db = get_db()
        product = None
        try:
            with get_db_cursor(db) as cursor:
                cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
                result = cursor.fetchone()
                if result:
                    product = Product(id=result['id'], name=result['name'],
                                      description=result['description'], price=result['price'])
        except Exception as e:
            print("Error fetching product: {}".format(e))
        finally:
            db.close()
        return product

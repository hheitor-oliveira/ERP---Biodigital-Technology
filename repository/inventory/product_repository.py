# internal's import's
from database.connection import DatabaseConnection
from domain.inventory.product import Product

class ProductRepository:
    '''Reponsável por coordenar os processos de persistência da classe Product.'''
    def save(self, product: Product) -> None:

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO product (
                    product_name,
                    category_id,
                    cost_price,
                    sale_value
                )
                VALUES (%s, %s, %s, %s)
                """,    
                (
                    product.name,
                    product.category.id,
                    product.cost_price,
                    product.sale_value
                )
            )
    
            connection.commit()
    
        finally:
            connection.close()
            
            
    def reconstruct(self, product: Product):
        pass
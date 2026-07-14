# internal's import's
from database.connection import DatabaseConnection
from domain.inventory.product import Product


class ProductRepository:
# """Reponsável por registrar um produto no banco."""
    def save(self, product: Product) -> None:

        connection = DatabaseConnection.get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO product (
                    product_name,
                    product_category,
                    cost_price,
                    sale_price
                )
                VALUES (%s, %s, %s, %s)
                """,
                (
                    product.name,
                    product.category.value,
                    product.cost_price,
                    product.sale_value
                )
            )

            connection.commit()

        finally:
            connection.close()
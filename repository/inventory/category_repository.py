# internal's import's
from database.connection import DatabaseConnection
from domain.inventory.category import Category


class CategoryRepository:
  
  # Função responsável por salvar a criação de uma categoria.
  def save(self, category: Category) -> None:

    connection = DatabaseConnection.get_connection()

    try:
      cursor = connection.cursor()

      cursor.execute(
        '''
        INSERT INTO category (
          category_name
        )
        VALUES (%s)
        ''',
        (
          category.name,
        )
      )
      
      connection.commit()
    
    finally:
      connection.close()
      
  def reconstruct(self) -> list[Category]:
    
    connection = DatabaseConnection.get_connection()
    
    try:
      cursor = connection.cursor()

      cursor.execute(
        '''
        SELECT 
        category_id,
        category_name        
        FROM category
        ORDER BY category_id;
        '''
      )
    
      rows = list(cursor.fetchall())
      categories: list[Category] = []
      
      for row in rows:
        id = row[0]
        name = row[1]
        
        category = Category.restore(name, id)
        categories.append(category)
      
      return categories
        
    finally:
      connection.close()
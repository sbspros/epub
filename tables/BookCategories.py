from dataclasses import dataclass,field
from sql_tables.SqlBookCategories import SqlBookCategories
@dataclass
class BookCategories(SqlBookCategories):
    book_id=int=0
    category_id:int=0
    creatation_date:int=0
    modification_date:int=0    
    _table_name:str='book_categories'

    def parse_key(self, book, category):
        self.book_id=book
        self.category_id=category
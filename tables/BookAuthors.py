from dataclasses import dataclass,field
from sql_tables.SqlBookAuthors import SqlBookAuthors
@dataclass
class BookAuthors(SqlBookAuthors):
    book_id=int=0
    author_id:int=0
    creatation_date:int=0
    modification_date:int=0    
    _table_name:str='book_authors'

    def parse_key(self, book, author):
        self.book_id=book
        self.author_id=author
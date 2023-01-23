from dataclasses import dataclass,field
from sql_tables.SqlBookIdentifiers import SqlBookIdentifiers
@dataclass
class BookIdentifiers(SqlBookIdentifiers):
    book_id=int=0
    identifier_id:int=0
    creatation_date:int=0
    modification_date:int=0    
    _table_name:str='book_identifiers'

    def parse_key(self, book, identifier):
        self.book_id=book
        self.identifier_id=identifier
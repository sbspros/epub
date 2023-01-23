from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from tables.BookFile import BookFile
from tables.GoogleBookInfo import GoogleBookInfo
from tables.Authors import Authors
from tables.BookAuthors import BookAuthors
from tables.Categories import Categories
from tables.BookCategories import BookCategories
from tables.Identifiers import Identifiers
from tables.BookIdentifiers import BookIdentifiers
class CreateTables():
    def __init__(self,bc:BaseClass,conn:SqlConnector):
        self._bc=bc
        self._sql_conn=conn
        self.check_table(BookFile())
        self.check_table(GoogleBookInfo())
        self.check_table(Authors())
        self.check_table(BookAuthors())
        self.check_table(Categories())
        self.check_table(BookCategories())
        self.check_table(Identifiers())
        self.check_table(BookIdentifiers())

    def check_table(self,table): 
        if table.is_created(self._sql_conn)==False:
            table.create_table(self._bc,self._sql_conn)
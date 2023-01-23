from dataclasses import dataclass,field
from sql_tables.SqlAuthors import SqlAuthors
@dataclass

class Authors(SqlAuthors):
    author:str=field(init=False,default="")
    creatation_date:int=0
    modification_date:int=0    
    _table_name:str='authors'

    def parse_author(self,name):
        self.author=name
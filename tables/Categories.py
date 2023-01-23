from dataclasses import dataclass,field
from sql_tables.SqlCategories import SqlCategories
@dataclass
class Categories(SqlCategories):
    category:str=field(init=False,default="")
    creatation_date:int=0
    modification_date:int=0    
    _table_name:str='category'

    def parse_category(self,name):
        self.category=name
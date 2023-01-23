from dataclasses import dataclass,field
from sql_tables.SqlIdentifiers import SqlIdentifiers

@dataclass
class Identifiers(SqlIdentifiers):
    type:str=field(init=False,default="")
    identifier:str=field(init=False)
    creatation_date:int=0
    modification_date:int=0
    _table_name:str='identifiers'

    def parse_identifiers(self,type,identifier):
        self.type=type
        self.identifier=identifier
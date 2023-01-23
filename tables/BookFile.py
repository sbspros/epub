from dataclasses import dataclass,field
from sql_tables.SqlBookFile import SqlBookFile
@dataclass
class BookFile(SqlBookFile):
    _title:str=field(init=False,default="")
    _authors:str=field(init=False,default="")
    _file_location:str=field(init=False)
    _file_name:str=field(init=False)
    _download:str='False'
    _checked:str='False'
    _found:str='False'
    _creatation_date:int=0
    _modification_date:int=0    
    _references:list=field(init=False,default_factory=lambda : [])
    _table_name:str='file_books'


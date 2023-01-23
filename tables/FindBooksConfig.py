from dataclasses import dataclass,field
from tables.AppConfig import AppConfig
import yaml
import traceback


class YamlFailure(Exception):
    def __init__(self):
        self.msg = 'Yaml file failed to load'
        super().__init__(self.msg) 

@dataclass
class FindBooksConfig(AppConfig):
    _symbols:list=field(init=False,default_factory=list)    

    def parse_config_file(self):
        try:
            with open('yaml/config.yaml','r') as file:
                app_info=yaml.safe_load(file)
        except:
            print("\t"+":"+traceback.format_exc())
            raise YamlFailure()
        
        ##Database Setup
        self._schema_name=app_info['DataBase']['Schema']

        ## Letup Logging
        self._file_name=app_info['Logging']['fileName']
        self._log_level=app_info['Logging']['logLevel']

        self._find_books=app_info['BookSearch']
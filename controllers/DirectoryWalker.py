
from common.BaseClass import BaseClass
from abc import ABC,abstractmethod
import traceback
import os

class DirectoryWalker(ABC):

    def __init__(self,bc:BaseClass):
        self._bc=bc

    def walk_dir(self):
        for root, subdirs, files in os.walk(self._bc._config._find_books):
            for filename in files:
                file_path = os.path.join(root, filename)
                if self.file_type_check(filename):
                    self.act_on_file(filename,file_path,root)
             
    @abstractmethod
    def file_type_check():
        pass

    @abstractmethod
    def act_on_file(self,filename,file_path,root):
        pass


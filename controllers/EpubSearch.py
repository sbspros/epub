from controllers.DirectoryWalker import DirectoryWalker
from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from models.ParseBookFile import ParseBookFile
class EpubSearch(DirectoryWalker):
    def __init__(self,bc:BaseClass,conn:SqlConnector):
        self._bc=bc
        self._conn=conn
        super().__init__(self._bc)

        
    def file_type_check(self,filename:str)->bool:
        if filename.find('.epub')!=-1:
            return True
        return False

    def act_on_file(self,filename,file_path,root):
        book_file=ParseBookFile(self._bc)
        book=book_file.parse_book_file(filename,file_path,root)
        if book_file.book_search(book._title,book._authors,filename):
            book.insert(self._bc,self._conn)     
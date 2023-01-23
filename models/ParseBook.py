from common.BaseClass import BaseClass
import ebooklib
from ebooklib import epub
import traceback


class ParseBook():
    def __init__(self,bc:BaseClass,filename:str):
        self._bc=bc
        self._filename=filename

    def parse_epub(self,filename):
        refer_type=['ISBN','EISBN','EBOOKISBN']
        book_info={"title":"","authors":"","identifier":""}
        try:
            book = epub.read_epub(filename)
            book_info['title']=book.get_metadata('DC', 'title')[0][0]
            book_info['authors']=book.get_metadata('DC', 'creator')[0][0]      
            id_list=[]
            for id in book.get_metadata('DC', 'identifier'):
                book_id=str(id[0])
                keys=id[1].keys()
                for key in keys:

                    if str(id[1][key]).upper() in refer_type:
                        id_list.append({str(id[1][key]).upper():book_id})
            book_info['ids']=id_list
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
        return book_info

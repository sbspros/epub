import json
from urllib.request import urlopen
from common.BaseClass import BaseClass
from tables.GoogleBookInfo import GoogleBookInfo
import traceback
 
class GoogleBookSearch():
    def __init__(self,bc:BaseClass):
        self._bc=bc

    def search(self,in_author,in_title,word):
        book_list=[]
        try:
            api="https://www.googleapis.com/books/v1/volumes?q={word}+inauthor:{in_author}+intitle:{in_title}"\
                .format(in_author=in_author,in_title=in_title,word=word)
            resp = urlopen(api)
            book_data = json.load(resp)
            for item in book_data["items"]:
                book=GoogleBookInfo()
                book.parse(item['volumeInfo'])
                book_list.append(book)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
        return(book_list)

from common.BaseClass import BaseClass
from models.GoogleBookSearch import GoogleBookSearch
from connectors.SqlConnector import SqlConnector
from controllers.CreateTables import CreateTables

class FindBookInfo():
    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._conn=SqlConnector(self._bc,bc._config._schema_name)._conn
        CreateTables(self._bc,self._conn)

    def fix_author_name(self,name):

        if name.find(',')==-1:
            return name         
        author_split= name.split(",")
        return author_split[1].strip()+' '+author_split[0].strip()

    def split_title(self,title):
        words=title.split(" ")
        if len(words) >1:
            search_word=words[1]
            search_title=words[0]
        else:
            search_word=words[0]
            search_title=words[0]   
        return search_word, search_title   

    def book_found(self,title,author,file):
        book_search=GoogleBookSearch(self._bc)
        search_word,search_title=self.split_title(title)
        author=self.fix_author_name(author)
        search_author=author.split(" ")[0]
        for book in book_search.search(search_author,search_title,search_word):
            try:
                if title==book.title and author==book.authors[0]:
                    book.save_book(self._bc,self._conn,file)
                    return True     
                elif  title==book.title:
                    return True 
            except:
                self._bc.log.error("\t parseing book")
        return False       

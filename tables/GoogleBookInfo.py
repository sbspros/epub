from dataclasses import dataclass,field
from tables.Authors import Authors
from tables.BookAuthors import BookAuthors
from tables.Categories import Categories
from tables.BookCategories import BookCategories
from tables.Identifiers import Identifiers
from tables.BookIdentifiers import BookIdentifiers
from tables.BookCategories import BookCategories
from sql_tables.SqlGoogleBookInfo import SqlGoogleBookInfo

@dataclass
class GoogleBookInfo(SqlGoogleBookInfo):
    title:str=field(init=False,default="")
    subtitle:str=field(init=False,default="")
    authors:str=field(init=False,default="")
    publisher:str=field(init=False,default="")
    publishedDate:str=field(init=False,default="")  
    description:str=field(init=False,default="")  
    industryIdentifiers:str=field(init=False,default="")  
    readingModes:str=field(init=False,default="")  
    pageCount:str=field(init=False,default="")  
    printType:str=field(init=False,default="")  
    categories:str=field(init=False,default="")  
    averageRating:str=field(init=False,default="")  
    ratingsCount:str=field(init=False,default="")  
    maturityRating:str=field(init=False,default="")  
    allowAnonLogging:str=field(init=False,default="")  
    contentVersion:str=field(init=False,default="")  
    panelizationSummary:str=field(init=False,default="")  
    imageLinks:str=field(init=False,default="")  
    language:str=field(init=False,default="")  
    previewLink:str=field(init=False,default="")  
    infoLink:str=field(init=False,default="")  
    canonicalVolumeLink:str=field(init=False,default="")
    file:str=field(init=False,default="")
    _table_name:str='google_book_info'
    def parse(self,results):
        for key,value in results.items():
            setattr(self,key,value)

    def save_book(self,bc,conn,file):
        try:
            self.file=file
            self.key=self.insert(bc,conn)
            self.save_authors(bc,conn)
            self.save_categories(bc,conn)
            self.save_identifier(bc,conn)
        except:
            bc.log.error("Book fiaile to save")

    def save_authors(self,bc,conn):
        for author in self.authors:
            save_author=Authors()
            save_author.parse_author(author)
            key=save_author.in_database(bc,conn)
            if key == None:
                key=save_author.insert(bc,conn)
            book_auth=BookAuthors()
            book_auth.parse_key(self.key,key)
            book_auth.insert(bc,conn)

    def save_categories(self,bc,conn):
        for category in self.categories:
            save=Categories()
            save.parse_category(category)
            key=save.in_database(bc,conn)
            if key == None:
                key=save.insert(bc,conn)
            book_cat=BookCategories()
            book_cat.parse_key(self.key,key)
            book_cat.insert(bc,conn)

    def save_identifier(self,bc,conn):
        for identifier in self.industryIdentifiers:
            save=Identifiers()
            save.parse_identifiers(identifier['type'],identifier['identifier'])
            key=save.insert(bc,conn)
            book_ind=BookIdentifiers()
            book_ind.parse_key(self.key,key)
            book_ind.insert(bc,conn)
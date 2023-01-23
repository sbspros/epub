from tables.BookFile import BookFile
from models.ParseBook import ParseBook
from controllers.FindBookInfo import FindBookInfo
import traceback

class ParseBookFile():
    def __init__(self,bc):
        self._bc=bc


    def parse_book_file(self,filename,file_path,root):
        maybe_author= self.parse_file_author(file_path)
        book_file=BookFile()
        parser=ParseBook(self._bc,filename)
        try:
            book=parser.parse_epub(file_path)
            book_file._title=book['title'].replace("'","''")
            book_file._authors=book['authors'].replace("'","''")
            book_file._file_location=root.replace("'","''")
            book_file._file_name=filename.replace("'","''")
            book_file._references=book['ids']

        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            book_file._authors=maybe_author
            book_file._file_location=root.replace("'","''")
            book_file._file_name=filename.replace("'","''")
        return book_file


    def parse_file_author(self,file_path):
        pre_author=file_path.replace(self._bc._config._find_books+"/","")
        cut_to=pre_author.find('/')
        return pre_author[0:cut_to]

    def book_search(self,title,authors,filename):
        find_book=FindBookInfo(self._bc)
        return find_book.book_found(title,authors,filename)

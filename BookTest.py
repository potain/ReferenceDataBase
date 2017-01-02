"""Unit Test for Book

..:: moduleauthors:: Wang Bo <wangbomicro@gmail.com>
"""
from Exceptions import IllegalAuthorsException, IllegalIssueNumberException, \
    IllegalYearException
import Book
import unittest

class BookTest(unittest.TestCase):
    """Unit Test for JournalArticle"""
    
    _authors = ["Wang, Bo", "De Coster, Jeroen", "Wevers, Martine"]
        
    def setUp(self):
        self.book1 = Book("Gas leak rate study of MEMS", 
                                self._authors, 1990, 'publisher1');
        self.book2 = Book("Gas leak rate study of MEMS", 
                                self._authors, 2015, 'publisher2');
        
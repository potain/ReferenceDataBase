"""Unit Test for JournalArticle

..:: moduleauthors:: Wang Bo <wangbomicro@gmail.com>
"""
from Exceptions import IllegalAuthorsException, IllegalIssueNumberException, \
    IllegalYearException
import JournalArticle
import Publication
import unittest

class JournalArticleTest(unittest.TestCase):
    """Unit Test for JournalArticle"""
    
    _authors = ["Wang, Bo", "De Coster, Jeroen", "Wevers, Martine"]
        
    def setUp(self):
        self.journal1 = JournalArticle("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 1990);
        self.journal2 = JournalArticle("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 2015);
        
    def test__init__(self):
        self.assertRaises(IllegalAuthorsException, Publication, 
                          "Gas leak rate study of MEMS", ["Wang", "Bo, "], 
                          "journal of MEMS", 123, 1990)
        
        self.assertRaises(IllegalIssueNumberException, Publication, 
                               "Gas leak rate study of MEMS", self._authors, 
                               "journal of MEMS", -123, 1990)
        
        self.assertRaises(IllegalYearException, Publication, 
                               "Gas leak rate study of MEMS", self._authors, 
                               "journal of MEMS", 123, 90)
    
    def test__getter__(self):
        self.assertEqual("Gas leak rate study of MEMS", self.validArtical1.title)
        self.assertEqual(self._authors, self.validArtical1.authors)
        self.assertEqual(123, self.validArtical1.issueNumber)
        self.assertEqual(1990, self.validArtical1.year)
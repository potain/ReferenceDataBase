"""Unit Test for Publication Tracker

..:: moduleauthors:: Wang Bo <wangbomicro@gmail.com>
"""

from Exceptions import *
from Publication import *
import Book
import ConferencePaper
import JournalArticle
import unittest

class PublicationTrackerTest(unittest.TestCase):
    """Unit Test for Publication Tracker"""
    
    _authors = ["Wang, Bo", "De Coster, Jeroen", "Wevers, Martine"]
        
    def setUp(self):
        self.validArtical1 = Publication("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 1990)
        self.validArtical2 = Publication("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 2016)
        
        
        self.reference10yearOld = JournalArticle("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 1990);
        self.referenceLastYear = JournalArticle("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 2015);

        self.publication1 = JournalArticle("publication1", self._authors, 
                                           "journal of MEMS", 123, 2016);
        self.publication2 = Book("publication2", ["Eric, Steegmans"], 
                                 2014, "acco");
        self.publication3 = ConferencePaper("publication3", 
                                            ["Wang, Bo", "Ann, WitVrouw"],
                                            2012, "Transducers")
        self.publication4 = JournalArticle("publication4", 
                                           ["Archesis, Test", "Shengping, Mao"],
                                           "journal of MEMS", 123, 2010);
        self.publication5 = Book("publication5", 
                                 ["Els, Wang", "Oliever, Thus"], 
                                 2008, "Springer")
        self.publication6 = Book("publication6", 
                                 ["Hellen, Wang", "Ou, Helen"], 
                                 2006, "Springer")
        self.publication_SameAs1 = JournalArticle("publication1", self._authors,
                                                  "journal of MEMS", 123, 2016)
        self.publication_Terminated = JournalArticle("publication_T", 
                                                     self._authors, 
                                                     "journal of MEMS", 
                                                     123, 2012);
        self.publication_Terminated.terminate();
        
        self.publication1.addAsCites(self.publication3);
        self.publication2.addAsCites(self.publication3);
        self.publication5.addAsCitedBy(self.publication3);
        self.publication6.addAsCitedBy(self.publication3);
        self.publication4.addAsCites(self.publication6);
        
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
        
    def test__setter__(self):
        self.validArtical1.title = "testTitle"
        self.validArtical1.authors = ["Wang, Bo", "Li, Lei"]
        self.validArtical1.issueNumber = 911
        self.validArtical1.year = 2016
        self.assertEqual("testTitle", self.validArtical1.title)
        self.assertEqual(["Wang, Bo", "Li, Lei"], self.validArtical1.authors)
        self.assertEqual(911, self.validArtical1.issueNumber)
        self.assertEqual(2016, self.validArtical1.year)
        
        self.assertRaises(IllegalAuthorsException, setattr, self.validArtical1, 
                          "authors", ["Wang"])
        self.assertRaises(IllegalIssueNumberException, setattr, self.validArtical1, 
                          "issueNumber", -119)
        self.assertRaises(IllegalYearException, setattr, self.validArtical1, 
                          "year", -119)
        
    def test__str__(self):
        self.assertEqual("B. Wang, J. De Coster, M. Wevers, Gas leak rate study of MEMS, journal of MEMS, 123, 1990", self.validArtical1.__str__())
        
    def testIsValidAuthor(self):
        invalidAuthors = ["Einstein, ", "De Coster", "Einstein ", "Wang Bo"]
        validAuthors = ["Jeroen, De Coster",  "Wang, Bo"]
        self.assertNotIn(True, 
                         [Publication.isValidAuthor(author) 
                          for author in invalidAuthors])
        self.assertNotIn(False, 
                         [Publication.isValidAuthor(author) 
                          for author in validAuthors])
        
    def testIsValidAuthors(self):
        invalidAuthors = ['Einstein', ", De Coster", "Einstein, ", "Wang Bo"]
        validAuthors = ["Jeroen, De Coster",  "Wang, Bo"]
        self.assertFalse(Publication.isValidAuthors(invalidAuthors))
        self.assertTrue(Publication.isValidAuthors(validAuthors))
        
    def testIsValidIssueNumber(self):
        invalidIssueNumbers = [-3, 0]
        validIssueNumbers = [123, 193800]
        self.assertNotIn(True, [Publication.isValidIssueNumber(issueNumber) 
                                for issueNumber in invalidIssueNumbers])
        self.assertNotIn(False, [Publication.isValidIssueNumber(issueNumber) 
                                 for issueNumber in validIssueNumbers])
        
    def testIsValidYear(self):
        invalidYears = [1300, 2019, -2013, 0]
        validYears = [1994, 2016, 2017]
        self.assertNotIn(True, [Publication.isValidYear(year) 
                                for year in invalidYears])
        self.assertNotIn(False, [Publication.isValidYear(year)
                                 for year in validYears])
        
    def testGetAuthorNumber(self):
        self.assertEqual(3, self.validArtical1.getAuthorsNumber())
        
    def testGetAuthorsName(self):
        self.assertEqual(["B. Wang", "J. De Coster", "M. Wevers"], 
                         self.validArtical1.getAuthorsName())
        
    def testCaptializeTitle(self):
        self.validArtical1.captializeTitle()
        self.assertEqual("Gas Leak Rate Study Of Mems", 
                         self.validArtical1.title)
    
    def testIs10YearsOld(self):
        self.assertTrue(self.validArtical1.is10YearsOld())
        self.assertFalse(self.validArtical2.is10YearsOld())

if __name__ == "__main__":
    unittest.main()
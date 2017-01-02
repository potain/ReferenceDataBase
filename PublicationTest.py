"""Unit Test for Publication Tracker

..:: moduleauthors:: Wang Bo <wangbomicro@gmail.com>
"""

import unittest
from Publication import *
from Exceptions import *

class PublicationTrackerTest(unittest.TestCase):
    """Unit Test for Publication Tracker"""
    
    _authors = ["Wang, Bo", "De Coster, Jeroen", "Wevers, Martine"]
    
    def setUp(self):
        self.validArtical1 = Publication("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 1990)
        self.validArtical2 = Publication("Gas leak rate study of MEMS", 
                                self._authors, "journal of MEMS", 123, 2016)
        
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
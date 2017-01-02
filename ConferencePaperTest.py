"""Unit Test for ConferencePaper

..:: moduleauthors:: Wang Bo <wangbomicro@gmail.com>
"""
from Exceptions import IllegalAuthorsException, IllegalIssueNumberException, \
    IllegalYearException
import ConferencePaper
import unittest

class ConferencePaperTest(unittest.TestCase):
    """Unit Test for ConferencePaper"""
    
    _authors = ["Wang, Bo", "De Coster, Jeroen", "Wevers, Martine"]
        
    def setUp(self):
        self.ConferencePaper1 = ConferencePaper("Gas leak rate study of MEMS", 
                                self._authors, 1990, 'conference1');
        self.ConferencePaper2 = ConferencePaper("Gas leak rate study of MEMS", 
                                self._authors, 2015, 'conference12');
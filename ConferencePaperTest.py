"""Unit Test for ConferencePaper

..:: moduleauthors:: Wang Bo <wangbomicro@gmail.com>
"""
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
                                
    def test__getter__(self):
        self.assertEqual("Gas leak rate study of MEMS", self.ConferencePaper1.title)
        self.assertEqual(self._authors, self.ConferencePaper1.authors)
        self.assertEqual("conference1", self.ConferencePaper1.conference)
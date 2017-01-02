"""A class of JournalArtical as a special kind of publication. In addition to 
title, authors, year, JournalArtical have a journalName and a issueNumber.

..:: moduleauthor: WangBo <wangbomicro@gmail.com> 
..:: invar:  The issueNumber must be a valid issueNumber.
"""
from Exceptions import IllegalIssueNumberException, IllegalWeightException
import Publication

class JournalArticle(Publication):
    """Initialize this new journalArticle with given title, authors, journal,
    issueNumber and year.
      
     Pre: 
         The given issue number must be a valid number for an journal.
     Post: 
         The journal of this new publication is equal to the given journal.
     Post: 
         The issueNumber of this new publication is equal to the given 
         issueNumber number.
     
     Args: 
         title (str): The title of the publication.
         authors (list): The authors name of the publication
         year (int): The publish year.
         journal (str): The journal name the publication belongs to.
         issueNumber (int): The issueNumber of the journal.
     
     throws: 
         IllegalAuthorException if the given author is invalid
         IllegalIssueNumberException if the given issueNumber is invalid
         IllegalYearException if the given year is invalid
     """
    _weight = 1.0
    
    def __init__(self, title, authors, journal, issueNumber, year):
        super(JournalArticle, self).__init__(title, authors, year)
        if not self.isValidIssueNumber(issueNumber):
            raise IllegalIssueNumberException(issueNumber)
        self._issueNumber = issueNumber
        
        self._journal = journal
    
    @property
    def journal(self):
        """Return the journal name of this Publication.
        
        Returns:
            str: The journal name of this Publication.
        """
        return self.__journal
    
    @journal.setter
    def journal(self, journal):
        """Set the journal of the journalArticle as the given journal name.
        
        Args:
            journal (str): The journal name of this Publication
        """
        if not self.isValidIssueNumber(journal):
            self.__journal = journal
    
    @property
    def issueNumber(self):
        """Return the issueNumber of the Publication.
        
        Returns:
            int: The issueNumber of the Publication.
        """
        return self.__issueNumber
    
    @issueNumber.setter
    def issueNumber(self, issueNumber):
        """Set the issueNumber as the given issueNumber
        
        Args:
            issueNumber (int): The issueNumber of the Publication, has to be \
            not negative.
        """
        if not self.isValidIssueNumber(issueNumber):
            raise IllegalIssueNumberException(issueNumber)
        else:
            self.__issueNumber = issueNumber
    
    def isValidIssueNumber(self, issueNumber):
        """Check whether the given issueNumber is a valid issue number.
        
        The valid issueNumber should larger then zero.
        
        Args:
            issueNumber (int): The issueNumber need to be checked.
        Returns:
            bool: True if and only if the given issueNumber is not negative.
        """
        return issueNumber > 0
    

     
 
    
         
        

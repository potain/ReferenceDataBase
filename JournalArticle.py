"""A class of JournalArtical as a special kind of publication. In addition to 
title, authors, year, JournalArtical have a journalName and a issueNumber.

..:: moduleauthor: WangBo <wangbomicro@gmail.com> 
..:: invar:  The issueNumber must be a valid issueNumber.
"""
from Exceptions import IllegalIssueNumberException
import Publication

class JournalArticle(Publication):
    pass
    """
    if not self.isValidIssueNumber(issueNumber):
            raise IllegalIssueNumberException(issueNumber)
        else:
            self.__issueNumber = issueNumber
    """
    
    @property
    def journal(self):
        """Return the journal name of this Publication.
        
        Returns:
            str: The journal name of this Publication.
        """
        return self.__journal
    
    @journal.setter
    def journal(self, journal):
        """Set the journal of the Publication
        
        Args:
            journal (str): The journal name of this Publication
        """
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
    
    @classmethod
    def isValidIssueNumber(cls, issueNumber):
        """Check if the given issueNumber is valid.
        
        The valid issueNumber should larger then zero.
        
        Args:
            issueNumber (int): The issueNumber need to be checked.
            
        Returns:
            bool: True if the issueNumber is valid.
        """
        return issueNumber > 0
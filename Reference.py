"""Science Reference module.

.. moduleauthor:: Wang Bo <wangbomicro@gmail.com>
"""
from Exceptions import *
import datetime
import re

class Reference(object):
    """Class of reference to refer to an article in a scientific journal.
    
    The class involving title, authors, name of the journal, issue number of the
    journal and the year of publication.
    
    .. note::
        
        This class is maybe change later.
    
    """
    
    def __init__(self, title, authors, journal, issueNumber, year):
        """Initialize this new reference with given title, authors, journal, 
        issueNumber and year.
        
        Args:
            title (str): The title of the reference
            authors (list): The authors name of the reference
            journal (str): The journal name the reference belongs to
            issueNumber (int): The issueNumber of the journal.
            year (int): The publish year.
        """
        self.__title = title
        if not self.isValidAuthors(authors):
            raise IllegalAuthorsException(authors)
        else:
            self.__authors = authors
            
        self.__journal = journal
        
        if not self.isValidIssueNumber(issueNumber):
            raise IllegalIssueNumberException(issueNumber)
        else:
            self.__issueNumber = issueNumber
        
        if not self.isValidYear(year):
            raise IllegalYearException(year)
        else:
            self.__year = year
        
    @property
    def authors(self):
        """Returns the authors of this reference
        
        Returns:
            list: The authors of the reference.
        
        """
        return self.__authors
    
    @authors.setter
    def authors(self, authors):
        """Set the authors of the reference as given authors.
        
        Args:
            authors (list): The authors of this reference
        """
        if not self.isValidAuthors(authors):
            raise IllegalAuthorsException(authors)
        else:
            self.__authors = authors
        
    @property
    def title(self):
        """The title of the artical
        """
        return self.__title
    
    @title.setter
    def title(self, title):
        """Set the title of the reference as given title.
        
        Args:
            title (str): The title of this reference
        """
        self.__title = title
        
    @property
    def journal(self):
        """Return the journal name of this reference.
        
        Returns:
            str: The journal name of this reference.
        """
        return self.__journal
    
    @journal.setter
    def journal(self, journal):
        """Set the journal of the reference
        
        Args:
            journal (str): The journal name of this reference
        """
        self.__journal = journal
    
    @property
    def issueNumber(self):
        """Return the issueNumber of the reference.
        
        Returns:
            int: The issueNumber of the reference.
        """
        return self.__issueNumber
    
    @issueNumber.setter
    def issueNumber(self, issueNumber):
        """Set the issueNumber as the given issueNumber
        
        Args:
            issueNumber (int): The issueNumber of the reference, has to be \
            not negative.
        """
        if not self.isValidIssueNumber(issueNumber):
            raise IllegalIssueNumberException(issueNumber)
        else:
            self.__issueNumber = issueNumber
    
    @property
    def year(self):
        """Return the year of the reference.
        
        Returns (int): The year of the published reference.
        """
        return self.__year
    
    @year.setter
    def year(self, year):
        """Set the year of the reference.
        
        Args:
            year (int): The year of the reference published.
        """
        if not self.isValidYear(year):
            raise IllegalYearException(year)
        else:
            self.__year = year
    
    @classmethod
    def isValidAuthors(cls, authors):
        """Check if all the given authors name are valid.
        
        The valid name of the authors is given as last, first name.
        e.g., "Einstein, Albert".
        
        Args:
            authors (list): The names of the author need to be checked.
        
        Returns:
            bool: True if all the names are valid, false if at least one of 
            the names are invalid.
        """
        
        return False not in [cls.isValidAuthor(author) for author in authors]
    
    @classmethod
    def isValidAuthor(cls, author):
        """Check if the given single author name is valid.
        
        The valid name of the authors is given as last, first name.
        e.g., "Einstein, Albert".
        
        Args:
            author (str): The name of the author need to be checked.
            
        Returns:
            bool: True if the name is valid, false if the name are invalid.
        """
        return re.match('^[a-zA-Z ]{1,20}, [a-zA-Z][a-zA-Z ]{1,20}$', author) is not None
    
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
    
    @classmethod
    def isValidYear(cls, year):
        """Check if the given year is valid.
        
        Args:
            year (int): The year need to be checked.
        
        Returns:
            bool: True if the 1500<= year <= (currentYear + 1)
        
        """
        return year >= 1500 and year <= datetime.date.today().year + 1
    

    def getAuthorsNumber(self):
        """Returns the number of Authors of the reference.
        
        Returns:
            int: The number of Authors of the reference.
        
        """
        return len(self.authors)
    
    def getAuthorsName(self):
        """Returns an list of authors.
        
        The authors are repersented as strings consisting the authors's
        initial and the last name. e.g.: "A. Einstein"; 
        
        Returns:
            str: the authors names.
        """
        authorNameList = []
        for author in self.authors:
            last, first = author.split(", ")
            authorNameList.append(first[0].upper() + ". " + last)
        return authorNameList            
    
    def captializeTitle(self):
        """Set the first letter of each word of given string to uppercase.
        
        """
        self.title = ' '.join([word.capitalize() 
                              for word in self.title.split(" ")])

    def is10YearsOld(self):
        """Check if the reference is 10 years old.
        
        Returns:
            bool: True if the reference is more then 10 years old.
        """
        return self.year + 10 < datetime.date.today().year
    
    def __repr__(self):
        """The internal representation of the reference
        """
        return "Reference({title},{authors},{journal},{issueNumber},{year})".\
            format(title = self.title, authors = self.authors, 
                   journal = self.journal, issueNumber = self.issueNumber,
                   year = self.year)
    
    def __str__(self):
        """The string representation of the reference
        
        Retruns:
            str: The String representation of the reference
        """
        return "{authors}, {title}, {journal}, {issueNumber}, {year}".\
            format(authors = ', '.join(self.getAuthorsName()), title = self.title, 
                   journal = self.journal, issueNumber = self.issueNumber,
                   year = self.year)

if __name__ == "__main__":
    R1 = Reference("title", "Bo Wang", "MEMS", 12222, 1986)
    print dir(R1.authors)
    print R1.authors.__doc__

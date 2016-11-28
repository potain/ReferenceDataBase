"""Science Reference module.

.. moduleauthor:: Wang Bo <wangbomicro@gmail.com>
"""


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
        self.__authors = authors
        self.__journal = journal
        self.__issueNumber = issueNumber
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
        self.__authors = authors
        
    @property
    def title(self):
        """
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
            issueNumber (int): The issueNumber of the reference.
        """
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
            year (int): The year of the reference.
        """
        self.__year = year
        
    def isValidAuthors(self, authors):
        """Check if the authors name is valid.
        
        The valid name of the authors is given as last, first name.
        e.g., "Einstein, Albert".
        
        Args:
            authors (list): The names of the author need to be checked.
        
        Returns:
            bool: True if the names are valid, false if the names are invalid.
        """
        pass
    
    def isValidIssueNumber(self, issueNumber):
        """Check if the given issueNumber is valid.
        
        The valid issueNumber should larger then zero.
        
        Args:
            issueNumber (int): The issueNumber need to be checked.
            
        Returns:
            bool: True if the issueNumber is valid.
        """
        pass
    
    def isValidYear(self, year):
        """Check if the given year is valid.
        
        Args:
            year (int): The year need to be checked.
        
        Returns:
            bool: True if the 1000<=year<=2016
        
        """
        pass
    
    def getAuthorsNumber(self):
        """Returns the number of Authors of the reference.
        
        Returns:
            int: The number of Authors of the reference.
        
        """
        pass
    
    def getAuthorsName(self):
        """Returns an list of authors.
        
        The authors are repersented as strings consisting the authors's
        initial and the last name. e.g.: "A. Einstein"; 
        
        Returns:
            str: the authors names.
        """
        pass
    
    def captializeTitle(self, title):
        """Set the first letter of each word of given string to uppercase.
        
        Args:
            title (str): The givenStrings.
        
        """
        pass
    
    def is10YearsOld(self):
        """Check if the reference is 10 years old.
        
        Returns:
            bool: True if the reference is more then 10 years old.
        """
        pass
        
        
        
        
    
    
    
    
        
        
    
    
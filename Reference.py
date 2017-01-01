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
            __terminated (bool): Indicate whether the instance terminated.  
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
        
        #Initialize this article with empty cites and citedBy property. 
        self.cites = set()
        self.citedBy = set()
        
        self.__terminate = False
        self.__id = -1
        
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
    
    @property
    def id(self):
        """The unique id number that refer to this, the initial value is -1.
        
        """
        return self.__id
    
    @id.setter
    def id(self, val):
        """Set ths ID number of this.
        
        """
        self.__id = val
    
    def isTheSameAs(self, Other):
        """Check if the given reference is the same as this.
        
        Args:
            other (Reference): The reference to be checked.
        
        Returns: 
            (boolean) True if the authors, title, year and the class type of this 
            and other are all the same.
        """
        
        pass
    
    def alreadyCites(self, Other):
        """Check if the given Reference already in the citesSet of this.
        
        Args:
            Other (Reference): The reference to be checked.
            
        Returns:
            (boolean) True if and only if this publication has the given publication 
            as one of its elements in the cites Set.
        """
        pass
    
    def getAllCites(self):
        """Return a set collecting shallow copy of all references that 
        this reference has been cited.
        
        Returns:
            (set) the set of publications that this publication cited.
     
        """
        pass
    
    def canCites(self, Other):
        """Check if this can cites the other reference.
        
        Args:
            other (Reference): The reference to be checked.
            
        Returns: 
            (boolean) False if the given publication is not effective. 
            False if the given publication is newer than this publication 
            False if the given publication is the same as this. 
            Otherwise, true if and only if this publication and the given 
            publication is not yet terminated.
        """
        pass
    
    def addAsCite(self, other):
        """Add the given publication as cited publication of this publication.
        
        Args:
            other (Reference): The article to be add as cited article. 
        Post:   
             This publication has the given publication as one of its cited
             publication in its cites Set.
        Post: 
             The given publication reference this publication as one of its citedBy
             publication in its citedBy set.
        Throws: 
            IllegalArgumentException: This publication cannot have the given 
            publication as one of its cites publication. 
        """
        pass
    
    def removeAsCite(self, other):
        """Remove the given publication from the cites set attached to 
        this publication.
            
        Args:
            other (Reference): The publication to be removed.
            
        Post:
             This publication does not have the given publication as one of 
             its cited publication.
        Post: 
             If this publication has the given publication as one of its cited 
             publication, the given publication remove this publication from 
             its citedBy set.
        """
        pass
    
    def haveProperCites(self):
        """Check whether this publication has proper cites attached to it.
        
        Returns:
            (boolean) True if and only if this publication can have each of 
            its cites attached to it, and each of its cites references this 
            publication as their citedBy set element.
        """
        pass
    
    def alreadyCitedBy(self, other):
        """Check if this reference has already CitedBy the given Reference
        
        Args:
            other (Reference): The reference need to be checked.
        
        Returns:
            (boolean): True if and only if this publication has the given 
            publication as one of its elements in the citesBy Set.
        """
        pass
    
    def getAllCitedBy(self):
        """Return a set collecting shallow copy of all publication that cites 
        this publication.
        
        Returns:
            (set) the set of articles that cited this.
        """
        pass
    
    
    def canBeCitedBy(self, other):
        """ Check whether this publication can be cited by the given publication.
        
        Returns:
            (boolean): False if this publication is not effective or if the 
            given publication is older than this publication, or if the given 
            publication is the same as this, otherwise, true if and only if 
            this publication and the given publication is not yet terminated.
        """
        pass
    
    def addAsCiteBy(self, other):
        """Add the given publication as citedBy publication of this publication.
        
        Args:
            other (Reference): The publication to be add as citedBy publication.
            
        Post:
             This publication has the given publication as one of its citedBy 
             publication in its citedBy Set.
        Post: 
            The given publication reference this publication as one of its 
            cites publication in its cites set.
        throws:
            IllegalArgumentException This publication cannot have the given 
            publication as one of its citedBy article.
        """
        pass

    
    def removeAsCitedBy(self, other):
        """Remove the given publication from the citedBy set attached to this.
        
        Args:
            other (Reference): The publication to be removed from the citedBy 
            set.
        Post: 
            This publication dose not have the given publication as one of its 
            cetiedBy publication.
        Post: 
            If this publication has the given publication as one of its citedBy 
            publication, the given publication remove this publication from its 
            cites Set.
        """
        pass
    
    def isTerminated(self, other):
        """Check whether this publication is already terminated.
        """
        pass
    
    def terminate(self):
        """Terminate this publication.
        
        Post: 
            This publication is terminated.
        Post: 
            No publication are attached any longer to the cites set and citedBy 
            set of this Publication. The cites and citeBy set of those 
            publications also removed this publication.
        """
        pass
    
    def haveProperCitedBy(self):
        """ Check whether this publication has proper citedBy publication 
        attached to it.
        
        Returns: 
            True if and only if this publication can have each of its citedBy 
            attached to it, and each of its citedBy references this publication 
            as their cites set element.
        """
        pass
    
    
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
        
        Returns:
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

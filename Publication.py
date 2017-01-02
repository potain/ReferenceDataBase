"""A class of scientific publications, which involving title, authors,
year of publication and a ID number.

.. moduleauthor:: Wang Bo <wangbomicro@gmail.com>
"""
from Exceptions import *
import datetime
import re

class Publication(object):
    """Class of Publication to refer to an publication in a scientific journal.
    
        invar: 
            The year of the publication must be a valid year.
        invar: 
            The authors name of the publication must be valid names. 
            The name of an author is given as last name, first name, e.g., 
            “Einstein, Albert”.
        invar: 
            The publication must has a proper cites and proper citedBy property. 
    """
    
    def __init__(self, title, authors, year):
        """Initialize this new Publication with given title, authors, journal, 
        issueNumber and year.
        
        Args:
            title (str): The title of the Publication
            authors (list): The authors name of the Publication
            year (int): The publish year.
       
         Post: 
             The title of this new publication is equal to the given title.
         Post: 
             The authors of this new publication is equal to the given authors.
         Post: 
             The year of this new publication is equal to the give year.
              
         throws: 
             IllegalAuthorException if the given author is invalid
         throws: 
             IllegalYearException if the given year is invalid
    
        """
        self.__title = title
        if not self.isValidAuthors(authors):
            raise IllegalAuthorsException(authors)
        else:
            self.__authors = authors
        
        if not self.isValidYear(year):
            raise IllegalYearException(year)
        else:
            self.__year = year
        
        #Initialize this publication with empty cites and citedBy property. 
        self.cites = set()
        self.citedBy = set()
        
        self.__terminate = False
        self.__id = -1
        
    @property
    def authors(self):
        """Returns the authors of this publication
        
        Returns:
            list: The authors of the publication.
        
        """
        return self.__authors
    
    @authors.setter
    def authors(self, authors):
        """Set the authors of the publication as given authors.
        
        Args:
            authors (list): The authors of this publication
        """
        if not self.isValidAuthors(authors):
            raise IllegalAuthorsException(authors)
        else:
            self.__authors = authors
        
    @property
    def title(self):
        """The title of the publication
        """
        return self.__title
    
    @title.setter
    def title(self, title):
        """Set the title of the publication as given title.
        
        Args:
            title (str): The title of this publication
        """
        self.__title = title
        
    
    @property
    def year(self):
        """Return the year of the publication.
        
        Returns (int): The year of the published publication.
        """
        return self.__year
    
    @year.setter
    def year(self, year):
        """Set the year of the publication.
        
        Args:
            year (int): The year of the publication published.
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
        """Check if the given publication is the same as this.
        
        Args:
            other (Publication): The publication to be checked.
        
        Returns: 
            (boolean) True if the authors, title, year and the class type of this 
            and other are all the same.
        """
        return (self.authors == Other.authors) and (self.year == Other.year) \
            and (self.title == Other.title) and (type(self) == type(Other)) 
    
    def alreadyCites(self, Other):
        """Check if the given publication already in the citesSet of this.
        
        Args:
            Other (Publication): The publication to be checked.
            
        Returns:
            (boolean) True if and only if this publication has the given publication 
            as one of its elements in the cites Set.
        """
        return Other in self.cites
    
    def getAllCites(self):
        """Return a set collecting shallow copy of all publications that 
        this publication has been cited.
        
        Returns:
            (set) the set of publications that this publication cited.
     
        """
        return self.cites.copy()
    
    def canCites(self, Other):
        """Check if this can cites the other publication.
        
        Args:
            other (Publication): The publication to be checked.
            
        Returns: 
            (boolean) False if the given publication is not effective. 
            False if the given publication is newer than this publication 
            False if the given publication is the same as this. 
            Otherwise, true if and only if this publication and the given 
            publication is not yet terminated.
        """
        return (Other is not None) and (not self.isTheSameAs(Other)) \
            and (self.year >= Other.year) and (not self.isTerminated()) \
            and (not Other.isTerminated())
        
    
    def addAsCite(self, other):
        """Add the given publication as cited publication of this publication.
        
        Args:
            other (Publication): The publication to be add as cited publication. 
        Post:   
             This publication has the given publication as one of its cited
             publication in its cites Set.
        Post: 
             The given publication add this publication as one of its citedBy
             publication in its citedBy set.
        Throws: 
            IllegalArgumentException: This publication cannot have the given 
            publication as one of its cites publication. 
        """
        if (not self.canCites(other)):
            raise IllegalValueException("This Publication can not cites the given\
            Exception.")

        self.cites.add(other)
        other.citedBy.add(self)
    
    def removeAsCite(self, other):
        """Remove the given publication from the cites set attached to 
        this publication.
            
        Args:
            other (Publication): The publication to be removed.
            
        Post:
             This publication does not have the given publication as one of 
             its cited publication.
        Post: 
             If this publication has the given publication as one of its cited 
             publication, the given publication remove this publication from 
             its citedBy set.
        """
        if (self.alreadyCites(other)):
            self.cites.remove(other)
            other.citedBy.remove(self)
        
    def haveProperCites(self):
        """Check whether this publication has proper cites attached to it.
        
        Returns:
            (boolean) True if and only if this publication can have each of 
            its cites attached to it, and each of its cites Publications this 
            publication as their citedBy set element.
        """
        for publication in self.cites:
            if (not self.canCites(publication)):
                return False
            if (not publication.alreadyCitedBy(self)):
                return False
        return True
    
    def alreadyCitedBy(self, other):
        """Check if this Publication has already CitedBy the given Publication
        
        Args:
            other (Publication): The Publication need to be checked.
        
        Returns:
            (boolean): True if and only if this publication has the given 
            publication as one of its elements in the citesBy Set.
        """
        return other in self.citedBy
    
    def getAllCitedBy(self):
        """Return a set collecting shallow copy of all publication that cites 
        this publication.
        
        Returns:
            (set) the set of publications that cited this.
        """
        return self.citedBy.copy() 
    
    
    def canBeCitedBy(self, Other):
        """ Check whether this publication can be cited by the given publication.
        
        Returns:
            (boolean): False if this publication is not effective or if the 
            given publication is older than this publication, or if the given 
            publication is the same as this, otherwise, true if and only if 
            this publication and the given publication is not yet terminated.
        """
        return (Other is not None) and (not self.isTheSameAs(Other)) \
            and (self.year >= Other.year) and (not self.isTerminated()) \
            and (not Other.isTerminated())
        
    def addAsCiteBy(self, other):
        """Add the given publication as citedBy publication of this publication.
        
        Args:
            other (Publication): The publication to be add as citedBy publication.
            
        Post:
             This publication has the given publication as one of its citedBy 
             publication in its citedBy Set.
        Post: 
            The given publication Publication this publication as one of its 
            cites publication in its cites set.
        throws:
            IllegalArgumentException This publication cannot have the given 
            publication as one of its citedBy publication.
        """
        if (not self.canBeCitedBy(other)):
            raise IllegalValueException("This Publication can not be cited by the \
            given Exception.")

        self.citedBy.add(other)
        other.cites.add(self)

    def removeAsCitedBy(self, other):
        """Remove the given publication from the citedBy set attached to this.
        
        Args:
            other (Publication): The publication to be removed from the citedBy 
            set.
        Post: 
            This publication dose not have the given publication as one of its 
            cetiedBy publication.
        Post: 
            If this publication has the given publication as one of its citedBy 
            publication, the given publication remove this publication from its 
            cites Set.
        """
        if (self.alreadyCitedBy(other)):
            self.citedBy.remove(other)
            other.cites.remove(self)
    
    def isTerminated(self, other):
        """Check whether this publication is already terminated.
        """
        return self.__terminate
    
    def terminate(self):
        """Terminate this publication.
        
        Post: 
            This publication is terminated.
        Post: 
            No publication are attached any longer to the cites set and citedBy 
            set of this Publication. The cites and citeBy set of those 
            publications also removed this publication.
        """
        for citedPublication in self.getAllCites():
            if not citedPublication.isTerminated():
                self.removeAsCites(citedPublication)
        for publicationCitedThis in self.getAllCitedBy():
            if not publicationCitedThis.isTerminated():
                self.removeAsCitedBy(publicationCitedThis)
        self.isTerminated = True
        
    def haveProperCitedBy(self):
        """ Check whether this publication has proper citedBy publication 
        attached to it.
        
        Returns: 
            True if and only if this publication can have each of its citedBy 
            attached to it, and each of its citedBy Publications this publication 
            as their cites set element.
        """
        for publication in self.citedBy:
            if (not self.canBeCitedBy(publication)):
                return False
            if (not publication.alreadyCites(self)):
                return False
        return True
    
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
    def isValidYear(cls, year):
        """Check if the given year is valid.
        
        Args:
            year (int): The year need to be checked.
        
        Returns:
            bool: True if the 1500<= year <= (currentYear + 1)
        
        """
        return year >= 1500 and year <= datetime.date.today().year + 1
    

    def getAuthorsNumber(self):
        """Returns the number of Authors of the Publication.
        
        Returns:
            int: The number of Authors of the Publication.
        
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
        """Check if the Publication is 10 years old.
        
        Returns:
            bool: True if the Publication is more then 10 years old.
        """
        return self.year + 10 < datetime.date.today().year
    
    def __repr__(self):
        """The internal representation of the Publication
        """
        return "Publication({title},{authors},{journal},{issueNumber},{year})".\
            format(title = self.title, authors = self.authors, 
                   journal = self.journal, issueNumber = self.issueNumber,
                   year = self.year)
    
    def __str__(self):
        """The string representation of the Publication
        
        Returns:
            str: The String representation of the Publication
        """
        return "{authors}, {title}, {journal}, {issueNumber}, {year}".\
            format(authors = ', '.join(self.getAuthorsName()), title = self.title, 
                   journal = self.journal, issueNumber = self.issueNumber,
                   year = self.year)
    
    @classmethod
    def isValidWeight(self, weight):
        """Check if the given weight 
        
        Returns:
            bool: true if the given weight larger than 0.
        """
        return weight > 0
    
    @classmethod
    def setWeight(cls, val):
        """Set the publication weight to the given weight.
        
        Args:
            weight(double):The weight to be set for the book 
        """
        if not cls.isValidWeight(val):
            raise IllegalWeightException(val)
        cls._weight = val;
    
    @classmethod    
    def getWeight(cls):
        """Get the weight of this type of publication.
        
        Returns:
            (double): The weigh of the current publication type.
        """
        return cls._weight

if __name__ == "__main__":
    R1 = Publication("title", "Bo Wang", "MEMS", 12222, 1986)
    print dir(R1.authors)
    print R1.authors.__doc__

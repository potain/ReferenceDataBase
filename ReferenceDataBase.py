"""A class representing a reference database, i.e., a collection of publications.

..:: moduleauthor: Wang Bo <wangbomicro@gmail.com>
..:: invar: The ReferenceDataBase must have proper publications.
"""
from Exceptions import IllegalValueException, IllegalAuthorsException, \
    IllegalPublicationIdException
import re

class ReferenceDataBase(object):
    
    incrementID = 1001
    
    def __init__(self):
        """Initialize this new ReferenceDatabase with no publications attached 
        to it. Only set its incrementID to 1001 so all the ID of new added 
        publications start counting from 1001.
     
        Post: 
            No publications are attached to this ReferenceDataBase.
        """
        ReferenceDataBase.incrementID = 1001
        self._isTerminated = False
        self._publications = dict()        
    
    def isTerminated(self):
        """Check whether this DataBase is already terminated.
        """
        return self._isTerminated
    
    def terminate(self):
        """Terminate this DataBase.
         Post: This DataBase is terminated.
         Post: All publication belonging to this DataBase have been Removed.
        """
        if not self.isTerminated():
            self._publications.clear()
        self._isTerminated = True
    
    def hasPublication(self, publication):
        """Check whether this DataBase has the given publication as one of the 
        publications attached to it.
        
        Args:
            publication (publication): The publication to check.
        """
        return publication.getId() in self._publications
    
    def hasPublicationID(self, id):
        """Check whether publication with the given ID in the database.
        
        Args:
            id (int): The id to be checked.
            
        Returns:
            (boolean): True if the publication with given in the dataBase, 
            otherwise return false.    
        """
        if not self.hasPublicationID(id):
            raise IllegalPublicationIdException(id)
        return self._publications[id];
        
    def getPublicationWithID(self, id):
        """Get the publication in the database by the given ID.
        
        Args:
            id (int): The publication ID.
            
        Returns: 
            (Publication) The publication if the id in the database, otherwise return null.
        
        throws: 
            IllegalPublicationIdException: If the given ID do not exist in 
            the publication DataBase.
        """
        if not self.hasPublicationID(id):
            raise IllegalPublicationIdException("The given publicationID is not \
            valid")
        
        return self._publications[id];
    
    def hasProperPublication(self):
        """Check whether this DataBase has proper publications associated 
        with it.
     
        Returns:
            (boolean): True if and only if this DataBase can have each of its 
            publications as a element of its publications set.
        """
        for publication in self.getAllPublications():
            if not self.canHaveAsPublication(publication):
                return False
        return True
    
    def canHaveAsPublication(self, publication):
        """Check whether this Database can have the given publication as one 
        of its elements.
     
        Args:
        publication (Publication): The publication to check
     
        Return:
        (Boolean) False if the given publication is not effective.
        """
        return publication != None and not publication.isTerminated()
    
    def addAsPublication(self, publication):
        """Add the given publication to the set of publications attached to 
        this Database.
         
        Args:
            publication (Publication): The publication to be added.
        Post:
            This Database has the given publication as one of its publications.
        throws:
            IllegalArgumentException: The given publication is already attached 
            to the DataBase. The given publication can not be attached to the 
            DataBase.
        """
        if not self.canHaveAsPublication(publication) or \
        self.hasPublication(publication):
            raise IllegalValueException("The database can not have the given\
            publication.")
        
        publication.id = ReferenceDataBase.incrementID 
        ReferenceDataBase.incrementID += 1
        self._publications[publication.getId()] = publication

    
    def removePublication(self, publication):
        """Remove the given publication from the set of publications attached 
        to this DataBase.
         
        Args:
        publication (Publication):The publication to be removed.
        
        Post: This Database does not have the given publication as one of its 
            publications.
        Post: If this Database has the given publication as one of it 
            publications, the given publication terminated, the association 
            between this publication and all the other publication are removed.
        """
        if self.hasPublication(publication): 
            publication.terminate()
            self._publications.remove(publication.getId())
     
    
    def getAllPublication(self):
        """Return a set collecting all publications associated with this Database.
        """
        return self._publications.values()
    
    @staticmethod
    def isValidAuthor(author):
        """Check if the single authors name is valid. The valid name of an 
        author is given as initialOfFirstName. lastName, e.g., “A. Einstein”.
        
        Args:
            author (Str): The author name to be checked.
        
        Returns:
            (boolean): true if this is a valid author name.
        """
        return re.match('^[a-zA-Z ]{1,20}, [a-zA-Z][a-zA-Z ]{1,20}$', author) \
            is not None
    
    def findByAuthor(self, authorName):
        """Find all publications authored by an author.
        
        Args:
            authorName (str): The author name to be searched, given as 
            “initialOfFirstName. lastName”, e.g., A. Einstein.
        Returns:
            (set) all publications authored by an author.
        Throws: 
            IllegalArgumentException If the given authorName is not in format 
            "initialOfFirstName.lastName"
        """
        if not self.isValidAuthor(authorName):
            raise IllegalAuthorsException(authorName)
        
        referenceSet = set();
        for publication in self.getAllPublications():
            if authorName in publication.authorsNames:
                referenceSet.add(publication)
        return referenceSet;
        
    def findByTitleWord(self, word):
        """Returns all publications that have a given word in their title;
        
        Args:
            word (str): The word to be searched in title.
        Returns:
            (Set): Set of publications that have a given word in their title
        """
        referenceSet = set()
        for publication in self.getAllPublications():
            if word.lower() in publication.getTitle().lower():
                referenceSet.add(publication)
        return referenceSet;
    
    def addCitation(self, publicationId1, publicationId2):
        """Add a citation relationship of two publications. Given as a pair of 
        publication identifiers where the second represents an publication cited 
        by the first;
        
        Args:
            publicationID1 (int):The publication id that cites publication2.
            publicationID2 (int):The publication id that cited by publication1
        Throws: 
            IllegalArgumentException: The publication with publicationID is 
            not in the DataBase The publication1 can not cites publication2.
        """
        publication1 = self.getPublicationWithID(publicationId1)
        publication2 = self.getPublicationWithID(publicationId2)
        publication1.addAsCites(publication2)
    
    @classmethod
    def getCurrentIncrementID(cls):
        """Get the current incrementID.
        
        Returns: 
            (int) The current increment ID.
        """
        return ReferenceDataBase.incrementID
    
    @classmethod
    def setCurrentIncrementID(cls, ID):
        """Set the IncrementID to the given value.
        Args:
            ID (int): The id number to be set.
        Throws: 
            IllegalIncrementIDException: if the given ID is out of bound.
        """    
        ReferenceDataBase.incrementID = ID
    
    def authorCitationIndex(self, authorName):
        """Calculate the citation index of given author. 
        
        The citation index is defined as the weighted sum of the citations of 
        all the author's publications. The weight depend on the type of 
        publication the author is cited in.
        
        Args:
            authorName (str): The author name.
        Returns:
            (double) The author citation index. 
        """
        citationIndex = 0;
        publications = self.findByAuthor(authorName)
        for publication in publications:
            citationIndex += publication.getWeight()
        return citationIndex
    
    
    
        